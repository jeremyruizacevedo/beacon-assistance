# Generated by Django 2.2.3 on 2019-07-10 16:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0010_auto_20190710_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personevent',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
