# Generated by Django 4.2.13 on 2024-07-05 02:41

import datetime
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        (
            "taggit",
            "0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx",
        ),
        ("blog", "0002_alter_category_options_alter_post_options_post_image_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="tags",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 7, 5, 2, 41, 51, 684956, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
