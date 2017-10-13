from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField


# TODO: make get_children that way, that it supports the blogs
class HomePage(Page):

    def get_blog_intro(Page):
        # display 3 new blog entrys
        pass

    heading = models.CharField()
    subheading = models.CharField()
    intro = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('subheading'),
        FieldPanel('intro')
    ]
