# Generated by Django 4.2.13 on 2024-07-02 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meals", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="meals",
            name="slug",
            field=models.SlugField(blank=True, null=True),
        ),
    ]
