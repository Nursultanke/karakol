# Generated by Django 3.1.3 on 2020-12-17 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0013_remove_listing_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='user_id',
        ),
    ]
