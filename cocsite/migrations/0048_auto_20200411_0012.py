# Generated by Django 2.2.5 on 2020-04-10 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cocsite', '0047_auto_20200411_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='rk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cocsite.Risk'),
        ),
        migrations.AlterField(
            model_name='score',
            name='sc',
            field=models.IntegerField(blank=True),
        ),
    ]
