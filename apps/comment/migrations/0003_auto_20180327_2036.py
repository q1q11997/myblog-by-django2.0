# Generated by Django 2.0 on 2018-03-27 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20180318_1823'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('comment', '0002_auto_20180113_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('comment', models.TextField(verbose_name='评论')),
                ('comment_time', models.DateField(auto_now_add=True, verbose_name='评论时间')),
                ('agree', models.IntegerField(default=0, verbose_name='点赞次数')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.DO_NOTHING, to='login.User', verbose_name='评论用户')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
                'ordering': ['-comment_time'],
            },
        ),
        migrations.DeleteModel(
            name='CommentPost',
        ),
    ]