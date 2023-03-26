from django.shortcuts import render
from .models import Menu, Field
import json

def index(request):
    menus = Menu.objects.all().values()
    names = []
    for m in menus:
        names.append(m['name'])
    menus = json.dumps(list(menus))
    return render(request, 'main/index.html', {'menus' : menus, 'names':names})

def menu(request, p):
    names = p.split('/')
    m = Menu.objects.filter(name = names[0])[0]
    del names[0]
    fields = json.dumps(list(Field.objects.filter(table_id=m.id).values()))
    return render(request, 'main/menu.html', {'fields': fields, 'names': names, 'menu': m.name})


