# Generated by Django 4.2.6 on 2023-11-23 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APPFinal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='barrio',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='descripcion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='piso',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
