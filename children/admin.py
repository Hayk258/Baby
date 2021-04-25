from django.contrib import admin
from .models import InfoSite, Category , Person
from django.utils.safestring import mark_safe


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


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Category Peoples """

    list_display = ('id', 'title', 'status', 'get_image')
    readonly_fields = ('get_image', 'date')
    list_display_links = ('id', 'title')
    list_editable = ('status',)
    save_on_top = True
    search_fields = ('title',)
    prepopulated_fields = {'url': ('title',)}
    fieldsets = (
        ('Category name and url', {
            'fields': ('title', 'url')
        }),
        ('About Category', {
            'fields': ('about',)
        }),
        ('Status and Date', {
            'fields': ('status', 'date',)
        }),
        ('Photo', {
            'fields': ('photo', 'get_image')
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="90" height="70"')

    get_image.short_description = 'Photo'


admin.site.register(Person)