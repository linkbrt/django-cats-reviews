# Generated by Django 5.1.1 on 2024-10-01 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cats", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cat",
            name="age",
            field=models.IntegerField(verbose_name="Возраст (в месяцах)"),
        ),
        migrations.AlterField(
            model_name="cat",
            name="color",
            field=models.CharField(max_length=50, verbose_name="Цвет"),
        ),
    ]
