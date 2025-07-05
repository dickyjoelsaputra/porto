from django.contrib.postgres.fields import ArrayField
from django.db import models

from taggit.managers import TaggableManager
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.models import Image

# Create your models here.
class Portfolio(index.Indexed, models.Model):
    modal_id = models.CharField(max_length=255)
    # image = models.ImageField(upload_to="portfolio_images")
    image = models.ForeignKey(
        Image,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    category = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    project_link = models.URLField()
    description = models.TextField()
    tags = TaggableManager()

    panels = [
        FieldPanel("modal_id"),
        FieldPanel("image"),
        FieldPanel("category"),
        FieldPanel("title"),
        FieldPanel("project_link"),
        FieldPanel("description"),
        FieldPanel("tags"),
    ]

    def __str__(self):
        return self.title
