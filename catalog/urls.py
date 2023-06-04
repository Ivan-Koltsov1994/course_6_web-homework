from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, contacts, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, toggle_activity

app_name = CatalogConfig.name

urlpatterns = [

    path('', ProductListView.as_view(), name = 'product_list'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('product/toggle/<int:pk>', toggle_activity, name='toggle_activity'),
]