# Generated by Django 3.0.2 on 2020-01-03 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200103_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pablicationmodel',
            name='slug',
            field=models.SlugField(unique_for_date='title'),
        ),
    ]
