# Generated by Django 4.1.1 on 2022-09-14 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_home_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='updated',
        ),
    ]
