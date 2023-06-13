from django.http import HttpResponse
from datetime import datetime

def año_de_nacimineto(request, edad):
    nacimiento = (datetime.today().year) - edad
    return HttpResponse(f"Naciste aproximadamente el año {nacimiento}")