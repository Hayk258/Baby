from django.contrib import admin
from .models import InfoSite


@admin.register(InfoSite)
class InfoSiteAdmin(admin.ModelAdmin):
    """" My site Info """

    list_display = ('id', 'name', 'status')
    list_display_links = ('id', 'name')
    list_editable = ('status',)
    save_on_top = True
    search_fields = ('name',)
    fieldsets = (
        ('User name', {
            'fields': ('name',)
        }),
        ('Instagram and Facebook', {
            'fields': ('instagram_link', 'facebook_link',)
        }),
        ('Telegram and YouTube', {
            'fields': ('telegram_link', 'youtube_link',)
        }),
        ('Address and Phone', {
            'fields': ('address', 'phone_number',)
        }),
        ('Background and Status', {
            'fields': ('background', 'status',)
        })

    )