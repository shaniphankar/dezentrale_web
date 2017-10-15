from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel

# TODO: make get_children that way, that it supports the blogs
class HomePage(Page):
    heading = models.CharField(max_length=255)
    subheading = models.CharField(max_length=255)
    intro = models.TextField()
    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('subheading'),
        FieldPanel('intro')
    ]
