# Generated by Django 4.0.6 on 2023-05-24 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Trish', '0012_profile_facebook_url_profile_insatgram_url_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='insatgram_url',
            new_name='instagram_url',
        ),
    ]
