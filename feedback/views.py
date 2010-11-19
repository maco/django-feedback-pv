# Create your views here.
from django.contrib.sites.models import Site
from django.http import HttpResponse
from django.utils.encoding import force_unicode
from django.core.mail import mail_managers
from django.core.urlresolvers import reverse
from django.core.validators import validate_email

import json

from feedback.models import *

import settings

def sanitize(errors):
    dct = dict((str(k),list(force_unicode(a) for a in v)) for k,v in errors.items())
    return dct

def handle_ajax(request):
   if not request.POST:
      return HttpResponse(json.dumps({'error':'no post recieved'}))
   try:
	   if request.POST["body"].strip() != "...":
	   	   return HttpResponse(json.dumps({'errors':{'text': ['Sorry your browser failed the honeypot test.']}}))
		   
	   if request.POST["text"].strip() == "":
	   	   return HttpResponse(json.dumps({'errors':{'text': ['This field is required.']}}))
	   
	   f = Feedback()
	   f.site = Site.objects.get_current()
	   f.url = request.META.get("HTTP_REFERER", "")
	   f.subject = request.POST["subject"]
	   f.email = request.POST["email"]
	   f.text = request.POST["text"]
	   f.user =  None if request.user.is_anonymous() else request.user
	   f.request = repr(request)[0:Feedback.REQUEST_MAX_LEN]
	   
	   try:
	      if f.email.strip() != "":		   
	         validate_email(f.email)
	   except Exception, e:
	      return HttpResponse(json.dumps({"errors":{"email": ["That's not a valid email address."]}}))
	   
	   f.save()
	   
	   frominfo = f.email.strip()
	   if f.user != None:
	      if frominfo == "":
	   	    frominfo = f.user.email
	      try:
	   	    frominfo += " " + unicode(f.user.get_profile())
	      except:
	   	    pass
		
	   mail_managers('Feedback: ' + (f.text[0:20] if f.subject.strip() == "" else f.subject), 
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
