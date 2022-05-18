from django.shortcuts import render, get_object_or_404, redirect
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView, UpdateView, DetailView
from pprint import pprint
from mptt.models import MPTTModel, TreeForeignKey
from .models import WareHouseOrder, WareHouseOrderItem, Supplier, SupplyOrderItem, SupplyOrder,ClientOrderItem, ClientOrder
from location.models import Wilaya, Commune 
from inventory.models import Product, WareHouseItem , WareHouse
from .forms import WareHouseOrderForm, WareHouseOrderItemForm, ProductInternalOrder, SupplierForm, SupplyOrderForm, SupplyOrderItemForm, ClientOrderForm, ClientOrderItemForm, WarehouseOrderItemFormSet
from accounts.models import User 
from django.conf import settings
from django.forms import formset_factory, modelformset_factory, inlineformset_factory
from django.contrib import messages
from order.filters import WareHouseOrderFilter
from django_weasyprint import WeasyTemplateResponseMixin
from django_weasyprint.views import WeasyTemplateResponse 
import ssl, functools
from django_weasyprint.utils import django_url_fetcher

# User = settings.AUTH_USER_MODEL

# Create your views here.
##commande depot 
# InternalOrderItemFormSet = inlineformset_factory (
#     WareHouseOrder,
#     WareHouseOrderItem,
#     form = WareHouseOrderItemForm,
#     min_num=0,  # minimum number of forms that must be filled in
#     extra=0,  # number of empty forms to display
# )

def add_new_item(request, param=None):
    the_number = param
    print('the num ', param)
    return render(request, "snippets/item_row_form.html", {'the_number':the_number})


def warehouse_order_create(request):
    princpale = WareHouse.centrale.principale()
    warehouse_items = WareHouseItem.objects.filter(location=princpale)
    receivers = WareHouse.objects.filter(actif=True)
    order_form = WareHouseOrderForm(request.POST or None)
    # product_formset = inlineformset_factory (
    #     WareHouseOrder,
    #     WareHouseOrderItem,
    #     fields=("warehouse_item","quantity"),
    #     form = WareHouseOrderItemForm,
    #     min_num=1, 
    #     extra=0,
    # )
    
    formset = WarehouseOrderItemFormSet()
    if request.method == "POST":
        print('user form')
        order_form = WareHouseOrderForm(request.POST)
        if order_form.is_valid():
            new_order = order_form.save(commit=False)
            new_order.order_type = "BC"
            new_order.save()
            for item_form in formset:
                print('one')
                if item_form.is_valid():
                    item = item_form.save(commit=False)
                    # print('le item', item)
                    # print('le item type', type(item))
                    # print('le item warehouse_item', item.warehouse_item.product.price)
                    # print('le item price', item.price)
                    item.order = new_order
                    item.price = item.warehouse_item.product.price
                    item.save()
                else: 
                    messages.error(request, item_form.errors)
            return redirect('order:warehouse_order_bc_list')
        else: 
            messages.error(request, order_form.errors)
                    ###### add error message if not valid
    else :
        order_form = WareHouseOrderForm()
    context = {
        "formset": formset,
        "the_number" : 0,
        "receivers" :  receivers,
        "warehouse_items" :  warehouse_items,
        "order_form" : order_form
    }
    return render(request, "warehouse_order_create.html", context)


def warehouse_order_edit(request, pk):
    order= get_object_or_404(WareHouseOrder, id=pk)
    # product_formset = inlineformset_factory (
    #     WareHouseOrder,
    #     WareHouseOrderItem,
    #     fields=("warehouse_item","quantity"),
    #     form = WareHouseOrderItemForm,
    #     min_num=1, 
    #     extra=0,
    # )
    if request.method == "POST":
        formset = WarehouseOrderItemFormSet(
            request.POST, instance=order
        )
        if formset.is_valid():
            formset.save()
    else:
        formset = WarehouseOrderItemFormSet(
            instance=order
        )
    # if order.is_empty():
    #     return render(request, "basket.html", {"formset": None})

    return render(request, "warehouse_order_edit.html", {"formset": formset})



class WarehouseOrderDetailView(DetailView):
    model = WareHouseOrder
    template_name= "warehouse_order_detail.html"
#### PDF

class WarehouseOrderPdfView(DetailView):
    model = WareHouseOrder
    template_name= "warehouse_order_detail_pdf.html"

class CustomWeasyTemplateResponse(WeasyTemplateResponse):
    def get_url_fetcher(self):
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        return functools.partial(django_url_fetcher, ssl_context=context)
        
class WarehouseCustomPrintableView(WeasyTemplateResponseMixin, WarehouseOrderPdfView):

    response_class = CustomWeasyTemplateResponse
### listes commandes interne

def is_valid_queryparam(param):
    return param != '' and param is not None

def get_filtered_warehouse_orders(request):
    context = {}
    qs = WareHouseOrder.objects.all()

    receiver_id = request.GET.get('receiver')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    # context['brands'] = Brand.objects.filter( actif=True, brand_products__isnull=False, brand_products__in=qs).distinct().order_by('name')
    # context["product_categories"] = Category.objects.filter(level=0, actif=True)
    # context['tags'] = Tag.objects.filter(is_active = True, products__isnull=False)


    if is_valid_queryparam(receiver_id):
        # warehouse = WareHouse.objects.filter(name__icontains=receiver_id)
        qs = qs.filter(receiver__name__icontains=receiver_id)
        
    if is_valid_queryparam(start_date):
        qs = qs.filter(created__gte=start_date)
    if is_valid_queryparam(end_date):
        qs = qs.filter(created__lte=end_date)
    # if is_valid_queryparam(tag_id):
    #     context["selected_tag"] = Tag.objects.get(id=tag_id)
    #     print("ouiiii tagging",context["selected_tag"])
    #     qs = qs.filter(tag=tag_id)

    # if is_valid_queryparam(category_id):
    #     cat = Category.objects.get(id=category_id)
    #     context["selected_category"] = Category.objects.get(id=category_id)
    #     children = cat.get_children()
    #     context['tags'] = Tag.objects.filter(is_active = True, products__isnull=False, products__category__in = cat.get_descendants(include_self=True)).distinct().order_by('name')
    #     context['brands'] = Brand.objects.filter(actif=True, brand_products__isnull=False,brand_products__category__in = cat.get_descendants(include_self=True) ).distinct().order_by('name')
    #     qs = qs.filter(category__in=cat.get_descendants(include_self=True), actif=True)
    #     if children.count():
    #         context["product_categories"] = children
    #     else : 
    #         context["product_categories"] =  cat.get_siblings(include_self=True)
    # if is_valid_queryparam(order):
    #     qs = qs.order_by(order)
    print('qs')
    return {'qs': qs, 'context': context}



def products_view(request):
    context = get_filtered_warehouse_orders(request)['context']
    queryset = get_filtered_warehouse_orders(request)['qs']
    print( '==============',queryset, '==============')
    # new_req= request.GET.copy()
    # queryset = get_filtered_warehouse_orders(new_req)['qs']

    context['warehouseorders'] = queryset
    return render(request, 'products.html', context)

#  Filtres des commandes

class WarehouseOrderBcListView(ListView): 
    def get_queryset(self):
        return WareHouseOrder.objects.filter(order_type='BC')
    model = WareHouseOrder
    template_name = "warehouse_order_list.html"
    context_object_name= "warehouseorders"

class WarehouseOrderFfListView(ListView): 
    def get_queryset(self):
        return WareHouseOrder.objects.filter(order_type='FF')
    model = WareHouseOrder
    template_name = "warehouse_order_list.html"
    context_object_name= "warehouseorders"


def htmx_order_bc_list(request):
    context = get_filtered_warehouse_orders(request)['context']
    queryset = get_filtered_warehouse_orders(request)['qs']
    return  render(request, "snippets/warehouse_order_list_block.html", {'warehouseorders' :queryset})

class WarehouseOrderBlListView(ListView): 
    def get_queryset(self):
        return WareHouseOrder.objects.filter(order_type='BL')
    model = WareHouseOrder
    template_name = "warehouse_order_list.html"
    context_object_name= "warehouseorders"

##commandes fournisseur 
### ajout d'un fournisseur 
class AddSupplierView(CreateView):
    template_name= "add-supplier.html"
    form_class= SupplierForm
    model = Supplier 
    success_url = reverse_lazy('order:supplier_order_bc_list')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)

class SupplierListView(ListView): 
    model = Supplier
    template_name = "supplier-list.html"
    context_object_name= "supplyers"

class SupplyOrderDetailView(DetailView):
    model = SupplyOrder
    template_name= "supplyorder-detail.html"
#### PDF
class SupplyOrderpdfView(DetailView):
    model = SupplyOrder
    template_name= "supplyorder-detail_pdf.html"

class CustomWeasyTemplateResponse(WeasyTemplateResponse):
    def get_url_fetcher(self):
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        return functools.partial(django_url_fetcher, ssl_context=context)
        
class SupplierCustomPrintableView(WeasyTemplateResponseMixin, SupplyOrderpdfView):

    response_class = CustomWeasyTemplateResponse

### listes commandes fournisseur
class SupplierOrderBcListView(ListView): 
    model = SupplyOrder
    template_name = "supplier-order-bc-list.html"
    context_object_name= "supplyorders"

class SupplierOrderBrListView(ListView): 
    model = SupplyOrder
    template_name = "supplier-order-br-list.html"
    context_object_name= "supplyorders"


def create_supplier_order(request):
    princpale = WareHouse.centrale.principale()
    items = WareHouseItem.objects.filter(location=princpale)
    suppliers = Supplier.objects.all()
    order_form = SupplyOrderForm(request.POST or None)
    product_formset = inlineformset_factory (
        SupplyOrder,
        SupplyOrderItem,
        fields=("warehouse_item","quantity"),
        form = SupplyOrderItemForm,
        min_num=1, 
        extra=0,
    )
    formset = product_formset(request.POST or None)
    if request.method == "POST":
        print('user form')
        order_form = SupplyOrderForm(request.POST)
        if order_form.is_valid():
            new_order = order_form.save(commit=False)
            new_order.order_type = "BC"
            new_order.save()
            for item_form in formset:
                print('one')
                if item_form.is_valid():
                    item = item_form.save(commit=False)
                    item.order = new_order
                    item.save()
                else: 
                    messages.error(request, item_form.errors)
            return redirect('order:supplier_order_bc_list')
            
        else: 
            messages.error(request, order_form.errors)
                    
    else :
        order_form = SupplyOrderForm()
    context = {
        "formset": product_formset,
        "the_number" : 0,
        "products" :  items, 
        "suppliers" :  suppliers, 
        "order_form" : order_form
    }
    return render(request, "add-supplier-order.html", context)

##commandes client  
class ClientOrderDetailView(DetailView):
    model = ClientOrder
    template_name= "clientorder-detail.html"
#### PDF
class ClientOrderOrderPdfView(DetailView):
    model = ClientOrder
    template_name= "clientorder-detail_pdf.html"

class CustomWeasyTemplateResponse(WeasyTemplateResponse):
    def get_url_fetcher(self):
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        return functools.partial(django_url_fetcher, ssl_context=context)
        
class ClientCustomPrintableView(WeasyTemplateResponseMixin, ClientOrderOrderPdfView):
    response_class = CustomWeasyTemplateResponse
### listes commandes client
class clientOrderBcListView(ListView): 
    model = ClientOrder
    template_name = "client-order-bc-list.html"
    context_object_name= "clientorders" 

class clientOrderFfListView(ListView): 
    model = ClientOrder
    template_name = "client-order-ff-list.html"
    context_object_name= "clientorders"

class clientOrderBlListView(ListView): 
    model = ClientOrder
    template_name = "client-order-bl-list.html"
    context_object_name= "clientorders"


def client_order_create(request):
    princpale = WareHouse.centrale.principale()
    items = WareHouseItem.objects.filter(location=princpale)
    communes= Commune.objects.all()
    deliverys = User.custom_objects.user_warehouses()
    order_form = WareHouseOrderForm(request.POST or None)
    product_formset = inlineformset_factory (
        ClientOrder,
        ClientOrderItem,
        fields=("warehouse_item","quantity"),
        form = ClientOrderItemForm,
        min_num=1, 
        extra=0,
    )
    formset = product_formset(request.POST or None)
    if request.method == "POST":
        print('user form')
        order_form = ClientOrderForm(request.POST)
        if order_form.is_valid():
            new_order = order_form.save(commit=False)
            new_order.order_type = "BC"
            new_order.save()
            for item_form in formset:
                print('one')
                if item_form.is_valid():
                    item = item_form.save(commit=False)
                    item.order = new_order
                    item.save()
                else: 
                    messages.error(request, item_form.errors)
            return redirect('order:client_order_bc_list')
            
        else: 
            messages.error(request, order_form.errors)
                 
    else :
        order_form = ClientOrderForm()
    context = {
        "formset": product_formset,
        "the_number" : 0,
        "products" :  items,
        "order_form" : order_form,
        "communes" : communes,
        "deliverys" : deliverys
    }
    return render(request, "add-client-order.html", context)

def client_order_edit(request):
    princpale = WareHouse.centrale.principale()
    items = WareHouseItem.objects.filter(location=princpale)
    communes= Commune.objects.all()
    deliverys = User.custom_objects.user_warehouses()
    order_form = WareHouseOrderForm(request.POST or None)
    product_formset = inlineformset_factory (
        ClientOrder,
        ClientOrderItem,
        fields=("warehouse_item","quantity"),
        form = ClientOrderItemForm,
        min_num=1, 
        extra=0,
    )
    formset = product_formset(request.POST or None)
    if request.method == "POST":
        print('user form')
        order_form = ClientOrderForm(request.POST)
        if order_form.is_valid():
            new_order = order_form.save(commit=False)
            new_order.order_type = "BC"
            new_order.save()
            for item_form in formset:
                print('one')
                if item_form.is_valid():
                    item = item_form.save(commit=False)
                    item.order = new_order
                    item.save()
                else: 
                    messages.error(request, item_form.errors)
            return redirect('order:client_order_ff_list')
            
        else: 
            messages.error(request, order_form.errors)
                 
    else :
        order_form = ClientOrderForm()
    context = {
        "formset": product_formset,
        "the_number" : 0,
        "products" :  items,
        "order_form" : order_form,
        "communes" : communes,
        "deliverys" : deliverys
    }
    return render(request, "edit-client-order.html", context)
## livraison  

class DeliveryListView(ListView): 
    model = WareHouseOrder
    template_name = "delivery-list.html"
    context_object_name= "warehouseorders"