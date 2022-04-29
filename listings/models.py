from django.db import models
from datetime import datetime

from category.models import Category
from realtors.models import Realtor
from django.contrib.auth.models import User

currency_items = [('сом', 'сом'), ('доллар', 'доллар'), ('евро', 'евро'), ('лира', 'лира'), ('рубль', 'рубль')]
categories_item = [('недвижимость', 'недвижимость'), ('авто', 'авто'), ('сельхоз', 'сельхоз'),
                   ('покупка/продажа', 'покупка/продажа'), ('работа', 'работа'), ('услуги', 'услуги'),
                   ('электроника', 'электроника'), ('попутчик', 'попутчик'), ('потеряли', 'потеряли'),
                   ('нашли', 'нашли')]


class Listing(models.Model):
    name = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    owner_name = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    price = models.IntegerField(blank=True)
    currency = models.CharField(max_length=50, choices=currency_items, verbose_name="цена в", blank=True)
    phone = models.CharField(max_length=100, blank=True)
    whatsapp_phone = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name="Категории", null=True,
                                 related_name='listings')
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
