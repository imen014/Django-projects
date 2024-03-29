# Generated by Django 4.2.3 on 2023-09-18 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('auteur', models.CharField(max_length=20)),
                ('annee_publication', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Liste_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(max_length=200)),
                ('quantitee', models.IntegerField()),
                ('prix', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Liste_Taches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=20)),
                ('terminee', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('contenu', models.CharField(max_length=200)),
            ],
        ),
    ]
