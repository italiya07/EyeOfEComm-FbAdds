# Generated by Django 3.2.13 on 2022-06-15 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adsapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
    ]