# Generated by Django 4.2.1 on 2024-05-27 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0009_women_husband'),
    ]

    operations = [
        migrations.AddField(
            model_name='husband',
            name='m_count',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
