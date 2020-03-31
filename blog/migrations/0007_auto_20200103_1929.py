# Generated by Django 3.0.2 on 2020-01-03 19:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200103_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='pablicationmodel',
            name='pablish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='pablicationmodel',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='thememodel',
            name='create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thememodel',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='thememodel',
            name='pablish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
