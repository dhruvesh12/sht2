# Generated by Django 2.0.9 on 2019-02-04 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_auto_20190204_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='infy',
            name='img',
            field=models.ImageField(default='no-photo.png', upload_to=''),
        ),
    ]
