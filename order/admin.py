from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import WareHouseOrder, WareHouseOrderItem, ClientOrder, ClientOrderItem, Supplier, SupplyOrder, SupplyOrderItem
import csv
import datetime
from import_export.admin import ImportExportModelAdmin, ExportMixin
from import_export import fields, resources, widgets



# class OrderResource(resources.ModelResource):
#     produits = fields.Field()
#     total_order = fields.Field(column_name="Totale Commande")
#     created = fields.Field(attribute="created",column_name="Crée le",widget=widgets.DateWidget(format = '%d-%m-%Y'))
#     paid = fields.Field(attribute="paid",column_name="Payé",widget=widgets.BooleanWidget())
#     class Meta:
#         model = WareHouseOrder
#         fields = ('id', 'user__username', 'first_name', 'phone', 'total_order','wilaya__name', 'commune__name', 'created', 'note', 'paid', 'confirmer', 'delivery_cost','produits')
#         export_order = ('id', 'user__username', 'first_name', 'phone', 'wilaya__name', 'commune__name', 'created', 'note', 'paid', 'confirmer',  'total_order', 'delivery_cost','produits')
#         widgets = {
#             'created': {'format': '%d-%m-%Y'},
#             }

#     def dehydrate_produits(self, order):
#         order_id = order.id
#         order= WareHouseOrder.objects.get(id=order_id)
#         products = []
#         for item in order.items.all():
#             products.append(item.product.reference) 
#         return ", ".join(products)

#     def dehydrate_total_order(self, order):
#         return order.get_total_order
        # exclude = ('updated', )

def order_detail(obj):
    url = reverse('order:admin_order_detail', args=[obj.id])
    return mark_safe(f'<a href="{url}">Detail</a>')

def order_pdf(obj):
    url = reverse('order:admin_order_pdf', args=[obj.id])
    return mark_safe(f'<a href="{url}">PDF</a>')
order_pdf.short_description = 'Invoice'


class WareHouseOrderItemInline(admin.TabularInline):
    model           = WareHouseOrderItem
    raw_id_fields   = ['warehouse_item']

# @admin.display()
# def total_da(obj):
#     return ("%s" % obj.get_total_cost())


@admin.register(WareHouseOrder)
class WareHouseOrderAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['id','receiver', 'created' ,'updated' ,'order_type', 'is_confirmed']
    list_display_links =('id', )
    list_filter = ['order_type','created','receiver',]
    list_editable = ['order_type', 'is_confirmed']
    # search_fields = ('first_name','last_name','phone','email')
    exclude = ('campany',)
    inlines = [WareHouseOrderItemInline] 
    list_per_page = 30
##client
class ClientOrderItemInline(admin.TabularInline):
    model           = ClientOrderItem
    raw_id_fields   = ['warehouse_item']

@admin.register(ClientOrder)
class ClientOrderAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['id','last_name', 'created' ,'updated' ,'order_type', 'is_confirmed']
    list_display_links =('id', )
    list_filter = ['order_type','created','last_name',]
    list_editable = ['order_type', 'is_confirmed']
    # search_fields = ('first_name','last_name','phone','email')
    exclude = ('campany',)
    inlines = [ClientOrderItemInline] 
    list_per_page = 30

#fournisseur 
class SupplyOrderItemInline(admin.TabularInline):
    model           = SupplyOrderItem
    raw_id_fields   = ['warehouse_item']

@admin.register(SupplyOrder)
class SupplyOrderAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['id','supplier', 'created' ,'updated' ]
    list_display_links =('id', )
    list_filter = ['created','supplier']
    # list_editable = [ 'is_confirmed']
    # search_fields = ('first_name','last_name','phone','email')
    exclude = ('campany',)
    inlines = [SupplyOrderItemInline] 
    list_per_page = 30


admin.site.register(Supplier) 
 