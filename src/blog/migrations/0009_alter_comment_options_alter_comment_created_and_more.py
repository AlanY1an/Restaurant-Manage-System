# Generated by Django 4.2.13 on 2024-07-05 08:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_alter_post_created_comment"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={"verbose_name": "Comment", "verbose_name_plural": "Comments"},
        ),
        migrations.AlterField(
            model_name="comment",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 7, 5, 8, 55, 12, 991757, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 7, 5, 8, 55, 12, 991026, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]