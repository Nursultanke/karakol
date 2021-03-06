# Generated by Django 3.1.3 on 2020-12-02 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20201202_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='categories',
            field=models.CharField(blank=True, choices=[('недвижимость', 'недвижимость'), ('авто', 'авто'), ('сельхоз', 'сельхоз'), ('покупка/продажа', 'покупка/продажа'), ('работа', 'работа'), ('услуги', 'услуги'), ('электроника', 'электроника'), ('попутчик', 'попутчик'), ('потеряли', 'потеряли'), ('нашли', 'нашли')], max_length=50, verbose_name='Категории'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='currency',
            field=models.CharField(blank=True, choices=[('сом', 'сом'), ('доллар', 'доллар'), ('евро', 'евро'), ('лира', 'лира'), ('рубль', 'рубль')], max_length=50, verbose_name='цена в'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='owner_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='listing',
            name='phone',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='whatsapp_phone',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
