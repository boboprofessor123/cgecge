# Generated by Django 2.2.5 on 2020-04-11 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cocsite', '0056_auto_20200411_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='rk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cocsite.Risk'),
        ),
        migrations.AlterField(
            model_name='result',
            name='introduction',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
