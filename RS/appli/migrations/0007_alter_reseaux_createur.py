# Generated by Django 4.0.4 on 2022-05-20 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appli', '0006_alter_reseaux_createur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reseaux',
            name='createur',
            field=models.CharField(max_length=100),
        ),
    ]
