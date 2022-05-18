from django.urls import path
from . import views 
from .views import AddProductView, ProductListView, ProductUpdateView,ProductDeleteView,  ProductDetailView
from .views import AddWarehouseView, WarehouseListView, WarehouseUpdateView
from .views import AddCategoryView, AddBrandView, BrandListView,  CategoryListView
from .views import  EditWarehouseItemView, WarehouseDetailView
from .views import ProductAnalyticsView, WarehouseAnalyticsView
from django.contrib.auth.decorators import login_required, permission_required
app_name= 'inventory'

urlpatterns = [ 
  
   #PRODUCT
   path('productlist', login_required(ProductListView.as_view()), name='productlist'),
   path('editproduct/<int:pk>/', login_required(ProductUpdateView.as_view()), name="editproduct"),
   path('productdetail/<int:pk>/', login_required(ProductDetailView.as_view()), name="productdetail"),
   path('productdelete/<int:pk>/', login_required(ProductDeleteView.as_view()), name="productdelete"),
   path('brandlist', login_required(BrandListView.as_view()), name='brandlist'),
   path('addbrand', login_required(AddBrandView.as_view()), name="addbrand"),
   path('addcategory', login_required(AddCategoryView.as_view()), name="addcategory"),
   path('categorylist', login_required(CategoryListView.as_view()), name='categorylist'),
   path('addproduct', login_required(AddProductView.as_view()), name="addproduct"),
   
   #WAREHOUSE 
   path('warehouselist', login_required(WarehouseListView.as_view()), name='warehouselist'),
   path('addwarehouse', login_required(AddWarehouseView.as_view()), name="addwarehouse"),
   path('editwarehouse/<int:pk>/', login_required(WarehouseUpdateView.as_view()), name="editwarehouse"),
   path('warehousedetail/<int:pk>/', login_required(WarehouseDetailView.as_view()), name="warehousedetail"),
   ##Warehouseitem
   path('editwarehouseitem/<int:pk>/', login_required(EditWarehouseItemView.as_view()), name="editwarehouseitem"),
   
   ## analytics 
   path('productanalytics', login_required(ProductAnalyticsView.as_view()), name='productanalytics'),
   path('warehouseanalytics', login_required(WarehouseAnalyticsView.as_view()), name='warehouseanalytics'),

]




