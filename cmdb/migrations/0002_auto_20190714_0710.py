# Generated by Django 2.2.3 on 2019-07-14 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilmReview',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('time', models.TextField(default=0)),
                ('content', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]