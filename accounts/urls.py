from django.urls import path
from accounts import views

urlpatterns = [
    path('register/', views.register, name='sign_up'),
    path('login/', views.auth_login, name='login')
]
