# Generated by Django 4.1.3 on 2022-12-14 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("funcionarios", "0002_rename_item_funcionarios"),
    ]

    operations = [
        migrations.CreateModel(
            name="Funcionario",
            fields=[
                ("id_Funcionario", models.AutoField(primary_key=True, serialize=False)),
                ("nome_Funcionario", models.CharField(max_length=100)),
                ("telefone", models.CharField(max_length=100)),
                ("sexo", models.CharField(max_length=100)),
                ("setor", models.CharField(max_length=11)),
                ("CPF", models.CharField(max_length=11)),
            ],
        ),
        migrations.DeleteModel(
            name="Funcionarios",
        ),
    ]