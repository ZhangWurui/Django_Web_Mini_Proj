# Generated by Django 2.2.3 on 2019-07-26 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0010_auto_20190714_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='preview_des',
            field=models.TextField(default='null', verbose_name='简介'),
        ),
    ]