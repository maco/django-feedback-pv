# Create your views here.
from django.contrib.sites.models import Site
from django.http import HttpResponse, HttpResponseForbidden
from django.utils.encoding import force_unicode
from django.core.mail import mail_managers
from django.core.validators import validate_email

import re
import json

from .models import *


def sanitize(errors):
    dct = dict((str(k), list(force_unicode(a) for a in v))
        for k,v in errors.items())
    return dct


def handle_ajax(request):
    if not request.POST:
        return HttpResponse(json.dumps({'error':'no post received'}))
    if request.META.get("REMOTE_ADDR", "") in getattr(settings, "FEEDBACK_BLOCKED_IPS", []):
        return HttpResponseForbidden("IP address blocked.")
    try:
        if not "body" in request.POST or request.POST["body"].strip() != "...":
            return HttpResponse(json.dumps({'errors':{'text':
                ['Sorry your browser failed the honeypot test.']}}))

        if request.POST["text"].strip() == "":
            return HttpResponse(json.dumps({'errors':{'text':
                ['This field is required.']}}))

        f = Feedback()
        f.site = Site.objects.get_current()
        f.url = request.META.get("HTTP_REFERER", "")
        f.subject = re.sub(r"\s", " ", request.POST["subject"])
        f.email = request.POST["email"]
        f.text = request.POST["text"]
        f.user =  None if request.user.is_anonymous() else request.user

        request_info = ""
        for key in ("HTTP_HOST", "REQUEST_URI", "HTTP_REFERER", "REMOTE_ADDR", "HTTP_USER_AGENT", "HTTP_COOKIE"):
            request_info += key + ": " + request.META.get(key, "") + "\n"
        f.request = request_info[0:Feedback.REQUEST_MAX_LEN]

        try:
            if f.email.strip() != "":
                validate_email(f.email)
        except Exception:
            return HttpResponse(json.dumps({"errors":{"email":
                ["That's not a valid email address."]}}))

        f.save()

        frominfo = f.email.strip()
        if f.user is not None:
            if frominfo == "":
                frominfo = f.user.email
            try:
                frominfo += " " + unicode(f.user.get_profile())
            except:
                pass

        mail_managers('Feedback: ' + (re.sub(r"\s", " ", f.text[0:20])
                                if f.subject.strip() == "" else f.subject),
                      'From: %s \n\n %s \n\n' %
                      (frominfo,
                       f.text,
                       #getattr(settings, 'SITE_ROOT_URL', "http://" + request.META["SERVER_NAME"]) + reverse('admin:feedback_feedback_change', args=[f.id])
                      ),
                      fail_silently=False)
        return HttpResponse(json.dumps({}))
    except Exception, e:
        import sys
        sys.stderr.write(str(e)+"\n")
        return HttpResponse(json.dumps({"error": str(e)}))
