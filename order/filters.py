import django_filters
from django_filters import DateRangeFilter,DateFilter
from .models import WareHouseOrder

class WareHouseOrderFilter(django_filters.FilterSet) :
    start_date = DateFilter() 
    end_date = DateFilter()
    # date_range = DateRangeFilter(field_name='created')
    class Meta: 
        model = WareHouseOrder
        fields = ['receiver', 'order_type', ]
    
   
  