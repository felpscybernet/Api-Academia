# Generated by Django 4.1.3 on 2022-12-14 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Fabricante",
            fields=[
                ("id_Fabricante", models.AutoField(primary_key=True, serialize=False)),
                ("nome_Fabricante", models.CharField(max_length=100)),
                ("CNPJ", models.CharField(max_length=14)),
                ("pais_de_Origem", models.CharField(max_length=100)),
                ("estado", models.CharField(max_length=100)),
                ("municipio", models.CharField(max_length=100)),
                ("data_de_Abertura", models.CharField(max_length=100)),
                ("codigo_Postal", models.CharField(max_length=100)),
                ("atividade", models.CharField(max_length=100)),
                ("socios", models.CharField(max_length=100)),
            ],
        ),
    ]
