# Generated by Django 3.0.6 on 2020-05-29 22:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_Achat', models.DateTimeField(default=django.utils.timezone.now)),
                ('quantite', models.IntegerField()),
            ],
            options={
                'ordering': ['date_Achat'],
            },
        ),
        migrations.CreateModel(
            name='Administrateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('login', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=20, verbose_name='Téléphone')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='E-Mail')),
                ('adresse', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['libelle'],
            },
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=50, unique=True)),
                ('designation', models.CharField(max_length=50)),
                ('prixU', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantite', models.IntegerField()),
                ('fournisseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Fournisseur')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('telephone', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=50)),
                ('produits', models.ManyToManyField(blank=True, through='API.Achat', to='API.Produit')),
            ],
        ),
        migrations.AddField(
            model_name='achat',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Client'),
        ),
        migrations.AddField(
            model_name='achat',
            name='produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Produit'),
        ),
    ]