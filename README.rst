Django Feedback App
===================
Based on jabapyth/django-feedback but significantly overhauled.

This app creates an ajax "feedback" button on your site, which pops up a form for
the user to fill in. The changes from jabapyth/django-feedback are as follows:

* Use the Colorbox Javascript library to display the popup reliably <http://colorpowered.com/colorbox/>.
* Store additional information in the database including the user if logged in and the full REQUEST object.
* Give the user his own email address as a default if he is logged in.
* Have the email also include information about the logged in user from get_profile().
* Refined the feedback tab image.
* Added a honypot field to prevent comment spam.
* Other cleanup.


Usage:
---------

Add 'feedback' to your site's list of apps and optionally set:

	EMAIL_SUBJECT_PREFIX = "[SITENAME] "

Run python manage.py syncdb to create the new table.
	
Add the feedback URLs to your URLconf, e.g.:

	(r'^feedback/', include('feedback.urls')),
	
Template modifications:

    <!-- in <head> -->
    {% include "feedback/header.html" %}
    
    <!-- in <body> -->
    {% include "feedback/button.html" %}

Symlink feedback/media into your static media directory as 'feedback'. The files
should be exposed as /media/feedback.

Feedback will be stored into the database and also emailed to the email addresses
listed in the MANAGERS setting.

