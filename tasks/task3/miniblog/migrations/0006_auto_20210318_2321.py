# Generated by Django 3.1.4 on 2021-03-18 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniblog', '0005_auto_20210318_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to='media/post_photo/'),
        ),
    ]