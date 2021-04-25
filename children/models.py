from django.core.validators import RegexValidator, MinLengthValidator
from django.db import models
from django.utils import timezone

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

class Category(models.Model):
    """ Categories peoples """

    title = models.CharField('Name Category', max_length=50, unique=True)
    about = models.TextField('About Category')
    photo = models.ImageField('Photo', upload_to='Category')
    url = models.SlugField('Url', max_length=50, unique=True)
    status = models.CharField('Status', choices=STATUS_CHOICES, default='published', max_length=10)
    date = models.DateTimeField('Date', auto_now_add=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Person(models.Model):
    """ Everything about Person """

    category_title = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='Category')
    first_name = models.CharField('Person Name', max_length=50)
    last_name = models.CharField('Person Last Name', max_length=50)
    middle_name = models.CharField('Person Middle name', max_length=50)
    disease = models.TextField('Name of disease')
    about = models.TextField('About Person')
    date_of_birth = models.DateTimeField('Person Born Date',)
    phone_number = models.CharField(unique=True, max_length=17,
                                    validators=[RegexValidator('^[0-9]*$'), MinLengthValidator(5)])
    email = models.EmailField('Person Email', unique=True, max_length=70)
    address = models.CharField('Person address', max_length=250, unique=True)
    url = models.SlugField('Url', max_length=50, unique=True)
    status = models.CharField('Status', choices=STATUS_CHOICES, default='published', max_length=10)
    photo = models.ImageField('Photo', upload_to=category_title)
    price = models.PositiveIntegerField('Price')

    def __str__(self):
        return self.first_name