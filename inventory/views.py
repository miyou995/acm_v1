from itertools import product
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import TemplateView
from django.views.generic import ListView, UpdateView, DetailView
from pprint import pprint
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib import messages
from location.models import Commune, Wilaya
from .models import Product, Category, Brand, WareHouse, WareHouseItem
from .forms import AddProductForm, AddBrandForm, AddCategoryForm, AddWareHouseForm, AddWareHouseItemForm
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.
## product

class ProductListView(ListView): 
    template_name= "product-list.html"
    model = Product 
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context["products"] =Product.objects.all().order_by('created')
        context["product_count"] =Product.objects.all().count()
        context["brands"] = Brand.objects.all()
        context["categorys"] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name= "product-detail.html"
    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        product_id = self.get_object().id
        context["products"] =Product.objects.all()
        context["warehouses"] = WareHouse.objects.all()
        context['warehouseitems'] = WareHouseItem.objects.all()
        context['instanceproduit'] = WareHouseItem.objects.filter(product=product_id)  
        context["wilayas"] = Wilaya.objects.all()
        context["communes"] = Commune.objects.all()
        return context 

class AddProductView(SuccessMessageMixin, CreateView):
    template_name= "add-product.html"
    form_class= AddProductForm
    model = Product 
    success_message = "Produit ajouté avec succès "
    success_url = reverse_lazy('inventory:productlist')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super(AddProductView, self).get_context_data(**kwargs)
        context["brands"] = Brand.objects.all()
        context["categories"] = Category.objects.all()
        return context 

class ProductUpdateView(SuccessMessageMixin,UpdateView):
    model = Product
    form_class= AddProductForm
    template_name = 'edit-product.html' 
    success_message = "Produit modifié avec succès "
    success_url = reverse_lazy('inventory:productlist')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context["brands"] = Brand.objects.all()
        context["categorys"] = Category.objects.all()
        return context 

class ProductDeleteView(SuccessMessageMixin, DeleteView):
    model = Product
    template_name= "delete-product.html"
    success_message = "Produit supprimé avec succès "
    success_url = reverse_lazy('inventory:productlist')


##category
class CategoryListView(ListView): 
    template_name= "category-list.html"
    model = Category 
    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context["categorys"] = Category.objects.all()
        context["category_count"] =Category.objects.all().count()
        return context

class AddCategoryView(SuccessMessageMixin, CreateView):
    template_name= "add-category.html"
    form_class= AddCategoryForm
    model = Category 
    success_message = "Catégorie ajouté avec succès "
    success_url = reverse_lazy('inventory:categorylist')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super(AddCategoryView, self).get_context_data(**kwargs)
        context["categorys"] = Category.objects.all()
        return context 

class EditCategoryView(SuccessMessageMixin, UpdateView):
    template_name= "edit-category.html"
    form_class= AddCategoryForm
    model = Category 
    success_message = "Catégorie modifié avec succès "
    success_url = reverse_lazy('inventory:categorylist')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super(AddCategoryView, self).get_context_data(**kwargs)
        context["categorys"] = Category.objects.all()
        return context 
class CategoryDeleteView(SuccessMessageMixin, DeleteView):
    model = Product
    template_name= "delete-category.html"
    success_message = "Catégorie supprimé avec succès "
    success_url = reverse_lazy('inventory:productlist')
##brand
class BrandListView(ListView): 
    template_name= "brand-list.html"
    model = Brand 
    success_url = reverse_lazy('inventory:brandlist')
    def get_context_data(self, **kwargs):
        context = super(BrandListView, self).get_context_data(**kwargs)
        context["brands"] = Brand.objects.all()
        context["brand_count"] =Brand.objects.all().count()
        return context
class AddBrandView(CreateView):
    template_name= "add-brand.html"
    form_class= AddBrandForm
    model = Brand 
    success_url = reverse_lazy('inventory:brandlist')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)

##warehouse
class WarehouseListView(ListView): 
    template_name= "warehouse-list.html"
    model = WareHouse 
    def get_context_data(self, **kwargs):
        context = super(WarehouseListView, self).get_context_data(**kwargs)
        context["warehouses"] = WareHouse.objects.all().order_by('created')
        context["warehouse_count"] = WareHouse.objects.all().count()
        context["wilayas"] = Wilaya.objects.all()
        context["communes"] = Commune.objects.all()
        return context

class AddWarehouseView(CreateView):
    template_name= "add-warehouse.html"
    form_class= AddWareHouseForm
    model = WareHouse 
    success_url = reverse_lazy('inventory:warehouselist')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super(AddWarehouseView, self).get_context_data(**kwargs)
        context["communes"] = Commune.objects.all()
        return context

class WarehouseUpdateView(UpdateView):
    model = WareHouse
    form_class= AddWareHouseForm
    template_name = 'edit-warehouse.html' 
    success_url = reverse_lazy('inventory:warehouselist')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)

class WarehouseDetailView(DetailView):
    model = WareHouse
    template_name= "warehouse-detail.html"
    def get_context_data(self, **kwargs):
        context = super(WarehouseDetailView, self).get_context_data(**kwargs)
        warehouse_id = self.get_object().id
        context["products"] =Product.objects.all().order_by('created')
        context['instanceproduit'] = WareHouseItem.objects.filter(location=warehouse_id)  
        context["brands"] = Brand.objects.all()
        context["categorys"] = Category.objects.all()
        return context 
## wraehouseitem
class EditWarehouseItemView(UpdateView):
    template_name= "edit-warehouseitem.html"
    form_class= AddWareHouseItemForm
    model = WareHouseItem 
    success_url = reverse_lazy('inventory:warehousedetail')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super(EditWarehouseItemView, self).get_context_data(**kwargs)
        context["products"] =Product.objects.all().order_by('created')
        context["warehouses"] = WareHouse.objects.all()
        return context 

## analytics

class ProductAnalyticsView(TemplateView):
    template_name= "product-analytics.html"

class WarehouseAnalyticsView(TemplateView):
    template_name= "warehouse-analytics.html"