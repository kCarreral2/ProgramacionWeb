from django.contrib import admin

# Register your models here.
from modelado.models import *


class ProductoAdmin(admin.ModelAdmin):
    fields = [('descripcion','precio'),('stock', 'iva')]
    list_display = ('descripcion','precio', 'stock','iva')
    search_fields = ('descripcion',)


admin.site.register(Producto,ProductoAdmin)
admin.site.register(Cliente)
admin.site.register(Factura)
admin.site.register(DetalleFactura)
