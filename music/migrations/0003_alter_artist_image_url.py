# Generated by Django 3.2.21 on 2023-09-14 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_artist_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='image_url',
            field=models.CharField(default='https://community.spotify.com/t5/image/serverpage/image-id/55829iC2AD64ADB887E2A5?v=v2', max_length=200),
        ),
    ]
