# Generated by Django 3.0.4 on 2020-03-28 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200103_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='pablicationmodel',
            name='pablic',
            field=models.CharField(max_length=50, null=True),
        ),
    ]