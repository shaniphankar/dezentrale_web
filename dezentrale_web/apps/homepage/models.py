from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField


class HomePage(Page):
    heading = models.TextField()
    subheading = models.TextField()
    intro = RichTextField()
    # FIXME: author as an user, not CharField
    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('subheading'),
        FieldPanel('intro')
    ]
