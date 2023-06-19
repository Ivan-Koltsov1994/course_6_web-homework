from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, toggle_activity, change_is_published, ContactView, ProductDescriptionUpdateView, \
    ProductCategoryUpdateView, CategoriesListView

app_name = CatalogConfig.name

urlpatterns = [

    path('', ProductListView.as_view(), name = 'product_list'),
    path('categories/', never_cache(CategoriesListView.as_view()), name='categories_list'),
    path('contacts/', never_cache(ContactView.as_view()), name='contacts'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>', never_cache(ProductUpdateView.as_view()), name='product_update'),
    path('product_update_description/<int:pk>/', never_cache(ProductDescriptionUpdateView.as_view()), name='product_description'),
    path('product_update_category/<int:pk>/', never_cache(ProductCategoryUpdateView.as_view()), name='change_description_product'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('product/toggle/<int:pk>', toggle_activity, name='toggle_activity'),
    path('is_published/<int:pk>/', change_is_published, name='change_is_published'),
]