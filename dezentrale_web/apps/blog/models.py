from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from modelcluster.fields import ParentalKey
import datetime


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('BlogPage', related_name='tagged_items')


class BlogPage(Page):
    content = models.CharField(max_length=255, blank=True, )
    #date = datetime.datetime.now()
    author = models.CharField(max_length=255, blank=True, )
   # tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('content', classname="full"),
        FieldPanel('author', classname="full"),
        #FieldPanel('tags'),
    ]


class BlogIndexPage(Page):
    intro = models.CharField(max_length=255, blank=True, )
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(BlogIndexPage, self).get_context(request, *args, **kwargs)

        # Add extra variables and return the updated context
        context['blog_entries'] = BlogPage.objects.descendant_of(self).live()
        return context



