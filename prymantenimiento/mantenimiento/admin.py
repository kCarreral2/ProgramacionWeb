from django.contrib import admin
from django.forms import Textarea
from django.contrib.admin import AdminSite
from mantenimiento.models import *

admin.site.register(Factura)
admin.site.register(DetalleFactura)
