# Generated by Django 4.1.5 on 2023-01-28 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='completed',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
