# Generated by Django 5.1.7 on 2025-07-05 05:13

import taggit.managers
import wagtail.search.index
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        (
            "taggit",
            "0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Portfolio",
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
                ("modal_id", models.CharField(max_length=255)),
                ("image", models.ImageField(upload_to="portfolio_images")),
                ("category", models.CharField(max_length=255)),
                ("title", models.CharField(max_length=255)),
                ("project_link", models.URLField()),
                ("description", models.TextField()),
                (
                    "tags",
                    taggit.managers.TaggableManager(
                        help_text="A comma-separated list of tags.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
            ],
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
    ]
