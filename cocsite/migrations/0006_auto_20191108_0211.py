# Generated by Django 2.2.7 on 2019-11-07 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocsite', '0005_auto_20191107_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='balance_loan',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customer',
            name='claim_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customer',
            name='claim_descript',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='customer',
            name='credit_level',
            field=models.CharField(default='A', max_length=5),
        ),
        migrations.AddField(
            model_name='customer',
            name='dividend_category',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='customer',
            name='fund_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='customer',
            name='insurance_category',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='customer',
            name='insurance_premiums',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customer',
            name='is_active',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='customer',
            name='is_blacklist',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customer',
            name='net',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='customer',
            name='percent',
            field=models.IntegerField(default=85),
        ),
        migrations.AddField(
            model_name='customer',
            name='period',
            field=models.IntegerField(default=12),
        ),
        migrations.AddField(
            model_name='customer',
            name='price_currency',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='customer',
            name='property_house',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='customer',
            name='situation',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='customer',
            name='usage',
            field=models.CharField(default='', max_length=20),
        ),
    ]
