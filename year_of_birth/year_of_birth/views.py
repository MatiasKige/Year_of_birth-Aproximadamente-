from django.http import HttpResponse
from datetime import datetime

def año_de_nacimineto(request, edad):
    año_actual = datetime.today().year
    nacimiento = año_actual - edad
    return HttpResponse("Naciste aproximadamente el año {año_actual}")