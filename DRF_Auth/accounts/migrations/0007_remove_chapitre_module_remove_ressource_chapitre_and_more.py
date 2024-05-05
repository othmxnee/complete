# Generated by Django 5.0.4 on 2024-05-05 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_chapitre_module_niveau_cours_commentaire_devoir_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapitre',
            name='Module',
        ),
        migrations.RemoveField(
            model_name='ressource',
            name='Chapitre',
        ),
        migrations.RemoveField(
            model_name='devoir',
            name='Chapitre',
        ),
        migrations.RemoveField(
            model_name='cours',
            name='Chapitre',
        ),
        migrations.RemoveField(
            model_name='mooc',
            name='Chapitre',
        ),
        migrations.RemoveField(
            model_name='commentaire',
            name='Cours',
        ),
        migrations.RemoveField(
            model_name='module',
            name='Promotion',
        ),
        migrations.RemoveField(
            model_name='promo',
            name='Niveau',
        ),
        migrations.DeleteModel(
            name='Fiche',
        ),
        migrations.DeleteModel(
            name='Ressource',
        ),
        migrations.DeleteModel(
            name='Devoir',
        ),
        migrations.DeleteModel(
            name='Chapitre',
        ),
        migrations.DeleteModel(
            name='Mooc',
        ),
        migrations.DeleteModel(
            name='Commentaire',
        ),
        migrations.DeleteModel(
            name='Cours',
        ),
        migrations.DeleteModel(
            name='Module',
        ),
        migrations.DeleteModel(
            name='Niveau',
        ),
        migrations.DeleteModel(
            name='Promo',
        ),
    ]
