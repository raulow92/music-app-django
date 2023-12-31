# Generated by Django 3.2.21 on 2023-09-14 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_alter_artist_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image_url',
            field=models.CharField(default='https://community.spotify.com/t5/image/serverpage/image-id/55829iC2AD64ADB887E2A5?v=v2', max_length=200),
        ),
        migrations.AlterField(
            model_name='artist',
            name='image_url',
            field=models.CharField(default='https://i.scdn.co/image/ab676161000051747baf6a3e4e70248079e48c5a', max_length=200),
        ),
    ]
