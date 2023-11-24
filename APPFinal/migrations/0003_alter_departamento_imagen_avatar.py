# Generated by Django 4.2.6 on 2023-11-23 23:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('APPFinal', '0002_alter_departamento_barrio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='avatares')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
