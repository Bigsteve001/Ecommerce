# Generated by Django 4.1.1 on 2022-09-15 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_home_trending_name_home_trending_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='shoename',
            field=models.CharField(max_length=200),
        ),
    ]