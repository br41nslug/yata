# Generated by Django 2.0.5 on 2019-05-24 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0046_chain_lastupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='faction',
            name='membersUpda',
            field=models.IntegerField(default=0),
        ),
    ]