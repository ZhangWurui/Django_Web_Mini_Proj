# Generated by Django 2.2.3 on 2019-07-14 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0009_auto_20190714_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='正文',
        ),
        migrations.RemoveField(
            model_name='article',
            name='预览图片',
        ),
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default='<p>null<p>', verbose_name='正文'),
        ),
        migrations.AddField(
            model_name='article',
            name='preview_Img',
            field=models.TextField(default='data:image/jpg;base64,', verbose_name='预览图片'),
        ),
    ]
