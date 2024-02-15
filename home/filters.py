import django_filters.rest_framework as filters
from home.models import Product

class ProductFilter(filters.FilterSet):
    min_instock = filters.NumberFilter(field_name="instock", lookup_expr='gte')
    max_instock = filters.NumberFilter(field_name="instock", lookup_expr='lte')
    tags = filters.CharFilter(field_name='tags__name')


    class Meta:
        model = Product
        fields = ['name','category']
