from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class BlogIndexPage(Page):
    intro = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    subpage_types = ['BlogPage']


class BlogPage(Page):
    content = models.TextField()
    author = models.CharField(max_length=255, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('content'),
        FieldPanel('author', classname="full"),
    ]

    parent_page_types = ['BlogIndexPage']
    subpage_types = []
