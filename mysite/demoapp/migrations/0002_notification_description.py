# Generated by Django 3.1.3 on 2020-11-08 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='description',
            field=models.CharField(default='hello', max_length=1500),
            preserve_default=False,
        ),
    ]
