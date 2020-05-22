# Generated by Django 2.2.5 on 2020-04-10 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cocsite', '0040_auto_20200410_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='ans1',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans2',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans3',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans4',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ques',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='fund',
            name='rk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cocsite.Risk'),
        ),
    ]