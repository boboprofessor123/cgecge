# Generated by Django 2.2.7 on 2019-11-08 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocsite', '0008_auto_20191108_0434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='carrer',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='dividend_category',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='education',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='service_units',
        ),
        migrations.AlterField(
            model_name='customer',
            name='uuid',
            field=models.CharField(max_length=40),
        ),
    ]