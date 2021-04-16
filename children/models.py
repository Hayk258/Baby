from django.core.validators import RegexValidator, MinLengthValidator
from django.db import models

STATUS_CHOICES = (
    ('published', 'Published'),
    ('draft', 'Draft'),
)


class InfoSite(models.Model):
    """ All info for my site """

    name = models.CharField('Name for info', max_length=30, unique=True)
    instagram_link = models.CharField('Instagram Link', max_length=100, unique=True, blank=True)
    facebook_link = models.CharField('Facebook Link', max_length=100, unique=True, blank=True)
    telegram_link = models.CharField('Telegram Link', max_length=100, unique=True, blank=True)
    youtube_link = models.CharField('YouTube Link', max_length=100, unique=True, blank=True)
    address = models.CharField('My address', max_length=250, unique=True, blank=True)
    background = models.ImageField('Background image', upload_to='background')
    phone_number = models.CharField(unique=True, max_length=17,
                                    validators=[RegexValidator('^[0-9]*$'), MinLengthValidator(5)], blank=True)
    status = models.CharField('Status', choices=STATUS_CHOICES, default='published', max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Info Site'
        verbose_name_plural = 'Info Site'