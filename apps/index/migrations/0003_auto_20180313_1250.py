# Generated by Django 2.0 on 2018-03-13 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20180127_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='music_url',
        ),
        migrations.AddField(
            model_name='music',
            name='music_id',
            field=models.IntegerField(default=0, verbose_name='歌曲id'),
        ),
    ]
