# Generated by Django 2.2.5 on 2020-04-10 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cocsite', '0034_auto_20200410_1459'),
    ]

    operations = [
        migrations.RenameField(
            model_name='score',
            old_name='rank',
            new_name='sc',
        ),
        migrations.AlterField(
            model_name='fund',
            name='rk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cocsite.Risk'),
        ),
    ]
