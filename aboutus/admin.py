from django.contrib import admin
from .models import About, SocialLink

# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count == 0:
            return True
        return False
    list_display = ("id", "title", "description")

class SocialLinkAdmin(admin.ModelAdmin):
    ordering = ("id",)
    list_display = ("id", "platform", "link")


admin.site.register(About, AboutAdmin)
admin.site.register(SocialLink, SocialLinkAdmin)
