# Generated by Django 3.2.8 on 2021-12-28 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faction', '0138_auto_20210605_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='attackchain',
            name='ranked_war',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='attackreport',
            name='ranked_war',
            field=models.BooleanField(default=False),
        ),
    ]
