# Create your models here.
from django.db import models

from wagtail.core.models import Page 
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.snippets.models import register_snippet
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.text import slugify


# Create your models here.

## Page que mostrará el index de las películas
## Hereda solo de Home y no descendientes

## Modelo para películas

class Coche(models.Model):
    marca = models.CharField('marca', max_length=250)
    modelo = models.CharField('modelo', max_length=250)
    year = models.CharField('year', max_length=250)
   

    panels = [
        FieldPanel('marca'),
        FieldPanel('modelo'),
        FieldPanel('year'),

    ]
    def __str__(self):
        return f'{self.marca} ({self.modelo})'
    
    class Meta:
        verbose_name = 'Coche'
        verbose_name_plural = 'Coches'
        


class CochesIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]

    def paginate(self, request, coches, *args):
        page = request.GET.get('page')
        
        paginator = Paginator(coches, 15)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        qs = ''
        
        coche = Coche.objects.all()

        context['coches'] = self.paginate(request, coche)
        context['qs'] = qs
        
        return context
    



    