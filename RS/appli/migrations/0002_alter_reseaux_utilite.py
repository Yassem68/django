# Generated by Django 4.0.4 on 2022-05-20 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appli', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reseaux',
            name='utilite',
            field=models.CharField(max_length=100),
        ),
    ]
