# Generated by Django 2.0.5 on 2018-05-27 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus_messages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulemsg',
            name='alarm_and_status',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='stringmsg',
            name='alarm_and_status',
            field=models.BigIntegerField(),
        ),
    ]