from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField


class BlogPage(Page):
    content = models.TextField()
    author = models.CharField(max_length=255, blank=True, )

    content_panels = Page.content_panels + [
        FieldPanel('content'),
        FieldPanel('author', classname="full"),
    ]


class BlogIndexPage(Page):
    intro = models.TextField()
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(BlogIndexPage, self).get_context(request, *args, **kwargs)

        # Add extra variables and return the updated context
        context['blog_entries'] = BlogPage.objects.descendant_of(self).live()
        return context
