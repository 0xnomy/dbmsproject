# Generated by Django 5.0.4 on 2024-05-05 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='DOB',
            field=models.DateField(default='1998-01-01'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='DOB',
            field=models.DateField(default='1980-01-01'),
        ),
    ]
