# Generated by Django 4.2.1 on 2024-05-23 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0007_tagpost_alter_women_cat_women_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Husband',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(null=True)),
            ],
        ),
    ]
