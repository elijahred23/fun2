# Generated by Django 4.0.2 on 2022-02-27 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='audioLength',
            field=models.DurationField(),
        ),
    ]