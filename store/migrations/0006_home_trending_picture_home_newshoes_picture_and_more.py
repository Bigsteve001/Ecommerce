# Generated by Django 4.1.1 on 2022-09-15 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_home_shoename'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='Trending_picture',
            field=models.ImageField(null=True, upload_to='trending/'),
        ),
        migrations.AddField(
            model_name='home',
            name='newshoes_picture',
            field=models.ImageField(null=True, upload_to='new/'),
        ),
        migrations.AddField(
            model_name='home',
            name='sale_picture',
            field=models.ImageField(null=True, upload_to='sale/'),
        ),
    ]
