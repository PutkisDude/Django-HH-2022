# Generated by Django 3.2 on 2022-05-31 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvseries', '0005_auto_20220531_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='name',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]