# Generated by Django 3.2 on 2022-05-31 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tvseries', '0007_auto_20220531_1952'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='serie',
            options={'ordering': ['name'], 'verbose_name': 'TV Serie', 'verbose_name_plural': 'Tv Series'},
        ),
    ]
