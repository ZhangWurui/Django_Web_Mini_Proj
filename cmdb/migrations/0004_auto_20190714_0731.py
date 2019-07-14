# Generated by Django 2.2.3 on 2019-07-14 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_auto_20190714_0715'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Categories', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='FilmReview',
        ),
    ]