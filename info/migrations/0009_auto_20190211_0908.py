# Generated by Django 2.0.9 on 2019-02-11 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0008_auto_20190211_0855'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='uservote',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='uservote',
            name='user',
        ),
        migrations.RemoveField(
            model_name='uservote',
            name='voter',
        ),
        migrations.DeleteModel(
            name='UserVote',
        ),
    ]
