# Generated by Django 2.2.7 on 2019-11-07 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocsite', '0006_auto_20191108_0211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='is_SYN',
        ),
    ]
