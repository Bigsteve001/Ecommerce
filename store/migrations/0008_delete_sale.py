# Generated by Django 4.1.1 on 2022-10-07 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_sale_shoe_trending_remove_home_trending_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='sale',
        ),
    ]
