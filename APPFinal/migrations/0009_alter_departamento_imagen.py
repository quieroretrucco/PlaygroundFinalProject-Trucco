# Generated by Django 4.2.6 on 2023-11-24 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APPFinal', '0008_alter_departamento_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]