from django.urls import path
from accounts import views
from django.contrib.auth.views import LoginView, LogoutView
from accounts.forms import LoginForm

urlpatterns = [
    path('register/', views.register, name='sign_up'),
    # path('login/', views.auth_login, name='account-login'),
    # path('logout/', views.auth_logout, name='account-logout'),
    path('login/', LoginView.as_view(template_name="accounts/login.html", authentication_form=LoginForm, 
                                     redirect_authenticated_user=True), name='account-login'),
    path('logout/', LogoutView.as_view(), name='account-logout'),
]
