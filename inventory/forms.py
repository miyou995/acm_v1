from django import forms
from django.forms import ModelForm
from .models import Product, Brand, Category, WareHouseItem, WareHouse


class AddProductForm(ModelForm) :
    class Meta: 
        model = Product 
        fields = ('name','upc','reference','category','brand','text','price','old_price','buy_price','actif','new',) 
        
class AddBrandForm(ModelForm) :
    class Meta: 
        model = Brand 
        fields = '__all__' 

class AddCategoryForm(ModelForm) :
    class Meta: 
        model = Category
        fields = '__all__' 

class AddWareHouseForm(ModelForm) :
    class Meta: 
        model = WareHouse
        fields = '__all__' 

class AddWareHouseItemForm(ModelForm) :
    class Meta: 
        model = WareHouseItem
        fields = '__all__' 


