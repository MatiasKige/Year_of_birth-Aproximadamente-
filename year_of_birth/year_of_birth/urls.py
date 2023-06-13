from django.contrib import admin
from django.urls import path
from year_of_birth.views import año_de_nacimineto

urlpatterns = [
    path('admin/', admin.site.urls),
    path("año-de-nacimiento/<int:edad>",año_de_nacimineto,name="año_de_nacimiento" )
]
