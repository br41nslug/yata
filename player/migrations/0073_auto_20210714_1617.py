# Generated by Django 3.1.5 on 2021-07-14 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0072_remove_player_bazaarupda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='error',
            name='short_error',
            field=models.TextField(default='-'),
        ),
    ]