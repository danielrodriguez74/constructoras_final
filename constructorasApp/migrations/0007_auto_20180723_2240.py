# Generated by Django 2.0.7 on 2018-07-24 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructorasApp', '0006_auto_20180723_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edificio',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
