from django.contrib import admin
from feedback.models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
	raw_id_fields = ("user", )


admin.site.register(Feedback, FeedbackAdmin)

# vim: et sw=4 sts=4
