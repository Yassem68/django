# Generated by Django 4.0.4 on 2022-05-20 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appli', '0003_createur_rename_nom_reseaux_nom_rs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reseaux',
            name='createur',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='appli.createur'),
        ),
    ]