# Generated by Django 4.2.13 on 2024-07-03 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meals", "0002_meals_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterModelOptions(
            name="meals",
            options={"verbose_name": "meal", "verbose_name_plural": "meals"},
        ),
    ]
