from django.db import models
from django import forms

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel,  MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet



from wagtail.search import index

class BlogIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        
        return context

    subpage_types = ['BlogPage','ViajesPage']
   
 

class BlogTagIndexPage(Page):
    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context
    subpage_types = []

class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

    

class BlogPage(Page):
    date = models.DateField("Fecha Post")
    intro = models.CharField("Introducción", max_length=250)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)


    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
            ],
            heading='Información'
        ),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', 
            label="Galería de imágenes"),
    ]

    parent_page_types = ['BlogIndexPage',]
    subpage_types = []
class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, 
        on_delete=models.CASCADE, 
        related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]

class ViajesTagIndexPage(Page):
    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        viajespage = ViajesPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['viajespage'] = viajespage
        return context

class ViajesPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'ViajesPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

class ViajesPage(Page):
    fecha = models.DateField("Fecha Post")
    intro = models.CharField("Introducción", max_length=250)
    cuerpo = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=ViajesPageTag, blank=True)
    categories = ParentalManyToManyField('blog.ViajesCategory', blank=True)
    coordenadas = models.CharField("Coordenadas", max_length=250, blank=True)

    content_panels = Page.content_panels + [
         MultiFieldPanel([
            FieldPanel('tags'),
            
            ],
            heading='Información'
        ),
     
        FieldPanel('intro'),
        FieldPanel('cuerpo', classname="full"),
        FieldPanel('fecha'),
        FieldPanel('coordenadas'),
        
    ]

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('cuerpo'),
    ]

    parent_page_types = ['BlogIndexPage',]
    subpage_types = []

@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categorías de blog'
        verbose_name = 'categoría de blog'

@register_snippet
class ViajesCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categorías de viajes'
        verbose_name = 'categoría de viajes'