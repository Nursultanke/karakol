# Generated by Django 3.1.3 on 2020-12-17 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(blank=True, default=2, on_delete=django.db.models.deletion.DO_NOTHING, to='category.category', verbose_name='Категории'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='categories',
            field=models.CharField(blank=True, max_length=100, verbose_name='Категории'),
        ),
    ]
