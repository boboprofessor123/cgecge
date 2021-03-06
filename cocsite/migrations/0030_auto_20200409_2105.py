# Generated by Django 2.2.5 on 2020-04-09 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cocsite', '0029_auto_20200409_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='ans1',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans3',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans4',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='fund',
            name='rk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cocsite.Risk'),
        ),
    ]
