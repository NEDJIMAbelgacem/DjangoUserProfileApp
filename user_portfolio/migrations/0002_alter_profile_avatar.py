# Generated by Django 4.1.1 on 2022-09-28 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default_profile_image.jpg', upload_to='profile_images'),
        ),
    ]