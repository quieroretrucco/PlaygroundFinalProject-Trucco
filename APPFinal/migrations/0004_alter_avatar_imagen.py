# Generated by Django 4.2.6 on 2023-11-24 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APPFinal', '0003_alter_departamento_imagen_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/avatares'),
        ),
    ]
