# Generated by Django 2.2.7 on 2019-11-07 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocsite', '0004_bbs_socialmedia'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='attr1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='attr2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='attr3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='attr4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='attr5',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='attr6',
            field=models.IntegerField(default=0),
        ),
    ]