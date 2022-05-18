from django import forms
from django.forms import ModelForm
from .models import WareHouseOrder, WareHouseOrderItem 
from .models import Supplier, SupplyOrder, SupplyOrderItem
from .models import ClientOrderItem, ClientOrder
from django.forms.models import inlineformset_factory, modelformset_factory



class WareHouseOrderForm(ModelForm) :
    class Meta: 
        model = WareHouseOrder
        fields = ('receiver', 'delivery_man', 'order_type', 'is_confirmed', 'is_paid', 'is_delivered', 'is_return', 'discount', 'delivery_cost', 'note')

class WareHouseOrderItemForm(ModelForm) :
    # custom = forms.IntegerField(required=False)
    class Meta: 
        model = WareHouseOrderItem
        fields = ("order","warehouse_item","quantity","price",)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
        # self.fields['custom'] = forms.IntegerField()

class ProductInternalOrder(forms.Form):
    product = forms.CharField( required=True)
    quantity = forms.IntegerField()
    # reference = 

#fournisseur 
class SupplyOrderForm(ModelForm) :
    class Meta: 
        model = SupplyOrder
        fields = '__all__'

class SupplierForm(ModelForm) :
    class Meta: 
        model = Supplier
        fields = '__all__'

class SupplyOrderItemForm(ModelForm) :
    custom = forms.IntegerField(required=False)
    class Meta: 
        model = SupplyOrderItem
        fields = ("order","warehouse_item","quantity","price",)

#client 
class ClientOrderForm(ModelForm) :
    class Meta: 
        model = ClientOrder
        fields = '__all__'

class ClientOrderItemForm(ModelForm) :
    custom = forms.IntegerField(required=False)
    class Meta: 
        model = ClientOrderItem
        fields = ("order","warehouse_item","quantity","price",)

from django.forms import BaseModelFormSet
class BaseAuthorFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = WareHouseOrderItem.objects.filter().distinct('warehouse_item')


WarehouseOrderItemFormSet = inlineformset_factory(
    WareHouseOrder,
    WareHouseOrderItem,
    fields=("warehouse_item","quantity",),
    form = WareHouseOrderItemForm,
    formset=BaseAuthorFormSet,
    min_num=1, 
    extra=0,
)