Django Feedback App by POPVOX (django-feedback-pv)
==================================================

Based on https://github.com/jabapyth/django-feedback but significantly overhauled.

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

---

Copyright (C) 2011 POPVOX.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
