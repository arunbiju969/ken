from django.contrib import admin
from .models import Slide, Announcement, SocialMediaLink, SiteSettings

# Register your models here.
admin.site.register(Slide)
admin.site.register(Announcement)
admin.site.register(SocialMediaLink)
admin.site.register(SiteSettings)
