# Generated by Django 3.0.1 on 2020-02-01 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faction', '0021_attacksreport_wall'),
    ]

    operations = [
        migrations.AddField(
            model_name='faction',
            name='chainsUpda',
            field=models.IntegerField(default=0),
        ),
    ]