# Generated by Django 2.2.7 on 2020-05-18 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cocsite', '0068_auto_20200518_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='rk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cocsite.Risk'),
        ),
    ]
