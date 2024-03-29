# Generated by Django 4.2.3 on 2023-09-18 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercicesmodeles', '0007_categories_produits_produit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('nom_pays', models.CharField(max_length=20)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_ville', models.CharField(max_length=50)),
                ('id_pays', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='exercicesmodeles.pays')),
            ],
        ),
    ]
