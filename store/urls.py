from django.urls import path
from .views import register_view, jwt_login_view, jwt_logout_view, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('accounts/login/', jwt_login_view, name='login'),
    path('logout/', jwt_logout_view, name='logout'),
]
