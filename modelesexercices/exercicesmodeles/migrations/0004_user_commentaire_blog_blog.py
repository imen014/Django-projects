# Generated by Django 4.2.3 on 2023-09-18 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercicesmodeles', '0003_recette_cuisine'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_user', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Commentaire_Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Commentaire', models.CharField(max_length=100)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercicesmodeles.user')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bloggueur', models.CharField(max_length=50)),
                ('contenu_blog', models.CharField(max_length=300)),
                ('id_commentaire', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='exercicesmodeles.commentaire_blog')),
            ],
        ),
    ]