# Generated by Django 2.0 on 2018-01-31 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-created_time'], 'verbose_name': '博客文章', 'verbose_name_plural': '博客文章'},
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='create_time',
            new_name='created_time',
        ),
    ]