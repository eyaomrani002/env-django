# Generated by Django 4.1.7 on 2023-03-07 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0004_fournisseur_adresse_fournisseur_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='produits',
        ),
        migrations.DeleteModel(
            name='ProduitNC',
        ),
        migrations.AlterField(
            model_name='categorie',
            name='name',
            field=models.CharField(choices=[('AL', 'Alimentaire'), ('Mb', 'Meuble'), ('Sn', 'Sanitaire'), ('Vs', 'Vaisselle'), ('Vt', 'Vêtement'), ('Jx', 'Jouets'), ('Lg', 'Linge de Maison'), ('Bj', 'Bijoux'), ('Dc', 'Décor')], default='AL', max_length=50),
        ),
        migrations.AlterField(
            model_name='fournisseur',
            name='nom',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='fournisseur',
            name='telephone',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.DeleteModel(
            name='Commande',
        ),
    ]