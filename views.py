from django.http import HttpResponse
import datetime
from django.template import Template, Context



def saludo(request):
    return HttpResponse('SALUDOS')

def segundo(request):
    return HttpResponse('ESTA ES LA SEGUNDA VISTA')

def diadehoy(request):
    dia = datetime.datetime.now()
    documento = f"Hoy es el dia: <br> {dia}"
    return HttpResponse(documento)

def minombreEs(self, nombre):
    documento = f"Mi nombre es: <br> {nombre}"
    return HttpResponse(documento)

def probandotemplate(self):
    nom= "Laura"
    ap= "Montoya Sanchez"
    diccionario= {"nombre":nom, "apellido":ap, "hoy":datetime.datetime.now()}
    miHtml = open("C:/Users/lauri/OneDrive/PYTHON/PythonProyecto1/Proyecto1/Proyecto1/plantillas/template1.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    micontexto = Context(diccionario)
    
    documento = plantilla.render(micontexto)
    return HttpResponse(documento)
    
    
