# Generated by Django 4.0.4 on 2022-05-20 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appli', '0005_alter_reseaux_createur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reseaux',
            name='createur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appli.createur'),
        ),
    ]
