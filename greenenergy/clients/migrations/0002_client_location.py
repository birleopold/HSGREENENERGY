# Generated by Django 3.1.7 on 2021-03-16 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
