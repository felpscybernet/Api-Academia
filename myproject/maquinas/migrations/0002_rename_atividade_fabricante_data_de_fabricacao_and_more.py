# Generated by Django 4.1.3 on 2022-12-14 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("maquinas", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="fabricante",
            old_name="atividade",
            new_name="data_de_fabricacao",
        ),
        migrations.RenameField(
            model_name="fabricante",
            old_name="data_de_Abertura",
            new_name="defeitos",
        ),
        migrations.RenameField(
            model_name="fabricante",
            old_name="estado",
            new_name="frete",
        ),
        migrations.RenameField(
            model_name="fabricante",
            old_name="municipio",
            new_name="modelo",
        ),
        migrations.RenameField(
            model_name="fabricante",
            old_name="socios",
            new_name="tempo_de_uso",
        ),
    ]
