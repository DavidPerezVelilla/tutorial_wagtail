from sqlite3 import Date
from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField
)
import datetime


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        noticias = noticia.objects.all().order_by('-date')[:5]
        context['noticias'] = noticias
        return context

    subpage_types = ['blog.BlogIndexPage', 'NoticiaIndexPage', 'ContactPage', 'pelis.PelisIndexPage', 'coches.CochesIndexPage']


class noticia (models.Model):
  
    titulo = models.CharField('titulo', max_length=250)
    contenido = models.CharField('contenido', max_length=1000)
    imagen = models.URLField(blank=True)
    pie = models.CharField('pie', max_length=500, blank=True)
    date = models.DateField('Fecha de la noticia',default=datetime.date.today, blank=True)

    panels = [
        FieldPanel('titulo'),
        FieldPanel('contenido'),
        FieldPanel('imagen'),
        FieldPanel('pie'),
        FieldPanel('date'),

    ]
    def __str__(self):
        return f'{self.titulo}'
    
    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

class NoticiaIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]



class FormField(AbstractFormField):
    page = ParentalKey(
        'ContactPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )


class ContactPage(AbstractEmailForm):

    template = "contact/contact_page.html"
    # This is the default path.
    # If ignored, Wagtail adds _landing.html to your template name
    landing_page_template = "contact/contact_page_landing.html"

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel("subject"),
        ], heading="Email Settings"),
    ]
    subpage_types = []
    