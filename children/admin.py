from django.contrib import admin
from .models import InfoSite, Category, Person
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


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):

    list_display = ('id', 'first_name', 'last_name', 'email', 'category_title', 'status', 'get_image')
    list_display_links = ('id', 'first_name')
    save_on_top = True
    list_editable = ('status',)
    search_fields = ('first_name', 'email', 'phone_number', 'address')
    readonly_fields = ('get_image',)
    list_filter = ('status', 'date', 'category_title', 'disease', 'city')
    fieldsets = (
        ('Category', {
            'fields': ('category_title',)
        }),
        ('Person name', {
            'fields': ('first_name', 'last_name', 'middle_name')
        }),
        ('Person info', {
            'fields': (('address', 'date_of_birth'), ('email', 'phone_number'),)
        }),
        ('Person photo and price', {
            'fields': (('price', 'photo', 'get_image'),)
        }),
        ('Person disease and about', {
            'fields': ('disease', 'about',)
        }),
        ('Url and status', {
            'fields': (('url', 'status'),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="90" height="70"')

    get_image.short_description = 'Photo'


admin.site.site_title = 'Hayk Admin'
admin.site.site_header = 'Hayk Admin'