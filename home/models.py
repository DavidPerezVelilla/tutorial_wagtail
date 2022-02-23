from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        noticias = noticia.objects.all()[:5]
        context['noticias'] = noticias
        return context

class noticia (models.Model):
  
    titulo = models.CharField('titulo', max_length=250)
    contenido = models.CharField('contenido', max_length=1000)
    imagen = models.URLField(blank=True)
    pie = models.CharField('pie', max_length=500, blank=True)

    panels = [
        FieldPanel('titulo'),
        FieldPanel('contenido'),
        FieldPanel('imagen'),
        FieldPanel('pie')

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

    def paginate(self, request, noticia, *args):
        page = request.GET.get('page')
        
        paginator = Paginator(noticia, 15)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages

   