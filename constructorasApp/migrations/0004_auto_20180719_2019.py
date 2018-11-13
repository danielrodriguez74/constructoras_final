# Generated by Django 2.0.7 on 2018-07-20 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructorasApp', '0003_apartamento_descripcion_general'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartamento',
            name='numero',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='apartamento',
            name='descripcion_general',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
