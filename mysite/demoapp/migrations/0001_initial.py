# Generated by Django 3.1.3 on 2020-11-08 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('link', models.CharField(blank=True, max_length=200)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('ntype', models.CharField(max_length=500)),
            ],
        ),
    ]
