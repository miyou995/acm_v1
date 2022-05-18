from django.urls import path
from . import views 
from location.views import WilayaView, CommuneView  
from django.contrib.auth.decorators import login_required, permission_required
app_name= 'location'

urlpatterns = [ 
  

   
   #commune wilaya 
  
   path('addwilaya', login_required(WilayaView.as_view()), name="addwilaya"),
   path('addcommune', login_required(CommuneView.as_view()), name="addcommune"),
 

 

]




