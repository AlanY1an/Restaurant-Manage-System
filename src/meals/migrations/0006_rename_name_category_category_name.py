# Generated by Django 4.2.13 on 2024-07-05 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("meals", "0005_alter_category_options"),
    ]

    operations = [
        migrations.RenameField(
            model_name="category", old_name="name", new_name="category_name",
        ),
    ]
