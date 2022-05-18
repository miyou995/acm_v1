from django.urls import path
from . import views 
from .views import client_order_create,client_order_edit, add_new_item,clientOrderBcListView,clientOrderFfListView,clientOrderBlListView, ClientOrderDetailView, ClientCustomPrintableView, warehouse_order_create, WarehouseOrderBcListView, WarehouseOrderFfListView,  WarehouseOrderBlListView, WarehouseOrderDetailView, WarehouseCustomPrintableView, create_supplier_order, SupplierOrderBcListView, SupplierOrderBrListView, AddSupplierView,SupplierListView, SupplyOrderDetailView, SupplierCustomPrintableView , DeliveryListView, warehouse_order_edit, htmx_order_bc_list
from django.contrib.auth.decorators import login_required, permission_required
app_name= 'order' 
 
urlpatterns = [
  
   path('add_new_item', add_new_item, name="add_new_item"),
   #commandes interne  
   path('warehouse_order_create', login_required(warehouse_order_create), name="warehouse_order_create"),
   path('warehouse_order_edit/<int:pk>', login_required(warehouse_order_edit), name="warehouse_order_edit"),
   path('warehouse_order_bc_list', login_required(WarehouseOrderBcListView.as_view()), name="warehouse_order_bc_list"),
   path('htmx_order_bc_list', login_required(htmx_order_bc_list), name="htmx_order_bc_list"),
   path('warehouse_order_ff_list', login_required(WarehouseOrderFfListView.as_view()), name="warehouse_order_ff_list"),
   path('warehouse_order_bl_list', login_required(WarehouseOrderBlListView.as_view()), name="warehouse_order_bl_list"),
   path('warehouseorder_detail/<int:pk>/', login_required(WarehouseOrderDetailView.as_view()), name="warehouseorder_detail"),
   path('warehouseorderpdf/<int:pk>/', login_required(WarehouseCustomPrintableView.as_view()), name="warehouseorderpdf"),
   #commandes fournisseur 
   path('create_supplier_order', login_required(create_supplier_order), name="create_supplier_order"),
   path('addsupplier', login_required(AddSupplierView.as_view()), name="addsupplier"),
   path('supplierlist', login_required(SupplierListView.as_view()), name="supplierlist"),
   path('supplier_order_bc_list', login_required(SupplierOrderBcListView.as_view()), name="supplier_order_bc_list"),
   path('supplier_order_br_list', login_required(SupplierOrderBrListView.as_view()), name="supplier_order_br_list"),
   path('supplyorder_detail/<int:pk>/', login_required(SupplyOrderDetailView.as_view()), name="supplyorder_detail"),
   path('supplyorderpdf/<int:pk>/', login_required(SupplierCustomPrintableView.as_view()), name="supplyorderpdf"),
   #commandes client 
   path('create_client_order', login_required(client_order_create), name="client_order_create"),
   path('client_order_edit', login_required(client_order_edit), name="client_order_edit"),
   path('client_order_bc_list', login_required(clientOrderBcListView.as_view()), name="client_order_bc_list"),
   path('client_order_ff_list', login_required(clientOrderFfListView.as_view()), name="client_order_ff_list"),
   path('client_order_bl_list', login_required(clientOrderBlListView.as_view()), name="client_order_bl_list"),
   path('clientorder_detail/<int:pk>/', login_required(ClientOrderDetailView.as_view()), name="clientorder_detail"),
   path('clientorderpdf/<int:pk>/', login_required(ClientCustomPrintableView.as_view()), name="clientorderpdf"),
   ## livraison  
   path('delivery_list', login_required(DeliveryListView.as_view()), name="delivery_list"),
]




