from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class home(Page):
    welcomeMessage = models.TextField()
    

    content_panels = Page.content_panels + [
        FieldPanel('welcomeMessage', classname="full")
    ]