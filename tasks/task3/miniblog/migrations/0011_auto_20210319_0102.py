# Generated by Django 3.1.4 on 2021-03-18 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniblog', '0010_auto_20210319_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='post_photo/'),
        ),
    ]