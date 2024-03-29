# Generated by Django 4.2.3 on 2023-09-18 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('types_champs_app', '0006_profils_utilisateurs_telecharger_fichiers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choix_produit', models.CharField(choices=[('EL', 'ELECTRONIQUE'), ('VM', 'VETEMENTS'), ('AL', 'ALIMENTATION')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choix', models.CharField(choices=[('CHM', 'CHOIX MULTIPLES'), ('CHO', 'CHOIX UNIQUES')], max_length=60)),
            ],
        ),
    ]
