# Generated by Django 4.2.6 on 2023-11-24 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APPFinal', '0006_alter_avatar_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagendepto/'),
        ),
    ]
