# Generated by Django 3.1.3 on 2020-11-08 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_notification_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
