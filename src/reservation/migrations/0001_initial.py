# Generated by Django 4.2.13 on 2024-07-03 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Reservation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.IntegerField()),
                ("number_of_persons", models.IntegerField()),
                ("date", models.DateField()),
                ("time", models.TimeField()),
            ],
        ),
    ]
