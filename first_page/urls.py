from django.urls import path
from .views import main_page, less_forms, product_detail, category_sort_id

app_name = 'main'

urlpatterns = [path('', main_page, name = 'main_page'),
               path('<int:id>/', category_sort_id, name = "category_sort"),
               path('product_detail/<int:id>/', product_detail, name = 'product_detail'),
               path('less_forms/', less_forms, name = 'less_forms')
]
