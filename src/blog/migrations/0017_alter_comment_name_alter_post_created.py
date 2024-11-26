# Generated by Django 4.2.13 on 2024-07-05 09:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0016_alter_post_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment", name="name", field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="post",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 7, 5, 9, 22, 11, 728017, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]