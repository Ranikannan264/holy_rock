from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet,product_list_view, product_detail_view
from . import views

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('api/products/', include(router.urls)),
    path('product/', product_list_view, name='product_list'),
    path('product/<int:pk>/', product_detail_view, name='product_detail'),
    path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),

]
