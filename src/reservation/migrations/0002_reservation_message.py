# Generated by Django 4.2.13 on 2024-07-04 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reservation", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="reservation",
            name="message",
            field=models.TextField(default="No message provided"),
            preserve_default=False,
        ),
    ]
