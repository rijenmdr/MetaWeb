from django.contrib import admin
from .models import Website,Visitor,MetaWebFeedback,PaidUser,Hotel
# Register your models here.
admin.site.register(Website)
admin.site.register(Visitor)
admin.site.register(MetaWebFeedback)
admin.site.register(PaidUser)
admin.site.register(Hotel)
