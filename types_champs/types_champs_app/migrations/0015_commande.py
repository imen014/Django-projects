# Generated by Django 4.2.3 on 2023-09-18 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('types_champs_app', '0014_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produits', models.ManyToManyField(to='types_champs_app.produit')),
            ],
        ),
    ]