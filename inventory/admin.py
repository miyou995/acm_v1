from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Category, Product, Brand, WareHouse, WareHouseItem
from import_export import resources
# Register your models here.


class WareHouseItemInline(admin.TabularInline):
    model = WareHouseItem

class WareHouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'commune','actif' ,'is_default')
    list_display_links = ('id','name' )
    list_per_page = 40
    list_editable = [ 'actif','is_default']
    search_fields = ('name',)
    inlines = [WareHouseItemInline]
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'actif')
    list_display_links = ('id','name' )
    list_per_page = 40
    list_editable = [ 'actif']
    search_fields = ('name',)

class WareHouseItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product',  'location', 'quantity')
    list_display_links = ('id','product' )
    list_per_page = 40
    # list_editable = [ 'actif']
    search_fields = ('product', 'location')

class CategoryAdmin(DjangoMpttAdmin):
    # def get_queryset(self, request):
    #     qs = super(CategoryAdmin, self).get_queryset(request)
    #     qs = qs.annotate(total_products=Product.objects.all(category__in=models.get_descendants(include_self=True)).count())
    #     return qs
    def count_products(self):
        return Product.objects.filter(category__in=self.get_descendants(include_self=True)).count()
    list_display = ('id', 'name', count_products, 'actif')
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('id','name' )
    list_per_page = 50
    list_editable = [ 'actif']
    search_fields = ('name',)
    exlude = ['slug']


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        # exclude = ('confirmer', )
        # widget = ManyToManyWidget(Country, field='name')
        fields = ('id','name', 'price', 'reference','category','text','old_price','brand','specifications')
        export_product = ('id', 'name', 'price', 'reference','category','text','old_price','brand','specifications')

class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'reference', 'upc','name', 'category', 'price', 'new',  'actif', )
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('id','name' )
    list_per_page = 40
    save_as = True
    list_filter = ( 'new', 'category')
    list_editable = ['category', 'price', 'new', 'reference', 'upc','actif']
    search_fields = ('name','reference','category__name', 'category__id')
    exclude  = ['is_facility', 'old_price']
    resource_class = ProductResource

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(WareHouse, WareHouseAdmin)
admin.site.register(WareHouseItem, WareHouseItemAdmin)