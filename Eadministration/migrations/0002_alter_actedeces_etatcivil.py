# Generated by Django 4.1.5 on 2023-01-28 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Eadministration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actedeces',
            name='EtatCivil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Eadministration.personne'),
        ),
    ]
