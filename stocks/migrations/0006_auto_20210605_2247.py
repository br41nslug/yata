# Generated by Django 3.1.5 on 2021-06-05 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0005_stock_torn_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='previous_market_cap',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='previous_total_shares',
            field=models.BigIntegerField(default=0),
        ),
    ]
