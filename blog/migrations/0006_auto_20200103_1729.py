# Generated by Django 3.0.2 on 2020-01-03 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200103_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pablicationmodel',
            name='image_content',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
