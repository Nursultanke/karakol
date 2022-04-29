# Generated by Django 3.1.3 on 2020-12-12 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
        ('listings', '0005_auto_20201202_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='realtor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.realtor'),
        ),
    ]