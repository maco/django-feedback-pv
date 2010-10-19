Feedback
========

creates an ajax "feedback" button on your site, which pops up a form for the
user to fill.

Usage:
---------

Add 'feedback' to your site's list of apps and optionally set these variables in settings.py:

	SITE_ROOT_URL = "http://www.example.com"
	EMAIL_SUBJECT_PREFIX = "[SITENAME] "

Run python manage.py syncdb to create the new table.
	
Add the feedback URLs to your URLconf, e.g.:

	(r'^feedback/', include('feedback.urls')),
	
Template modifications:

    <!-- in header block -->
    {% include "feedback/header.html" %}
    
    <!-- in body block -->
    {% include "feedback/button.html" %}

Symlink feedback/media into your static media directory as 'feedback'.

Feedback will also be emailed to the email addresses listed in the MANAGERS setting.

