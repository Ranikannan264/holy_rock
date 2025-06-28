
from django.urls import path
from .views import place_order,order_history,checkout_view,order_success

urlpatterns = [
    path('place/', place_order, name='place_order'),
    path('success/<int:order_id>/', order_success, name='order_success'),  
    path('history/', order_history, name='order_history'),
    path('checkout/',checkout_view , name='checkout'),
]
