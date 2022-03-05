'''
crear coches

ejecutar:

python manage.py shell < datos/crear_peliculas.py


python manage.py shell 
import sqlite3
%run datos/crearcoches.py
'''

from coches.models import Coche
from django.utils.text import slugify
import json
import os


# borrar pelis
for p in Coche.objects.all():
    p.delete()

#lista de películas del json
if os.path.exists("datos/coches.json"):
    coche = json.load(open("datos/coches.json"))
else:
    coche = json.load(open("coches.json"))


'''
[{"marca":"Subaru","modelo":"Impreza","year":2006},
'''

for p1 in coche:
    p = Coche()
    p.marca = p1["marca"]
    p.modelo = p1["modelo"]
    p.year = p1["year"]
    
    p.slug = slugify(f'{p.marca} ({p.modelo})')
    p.save()
