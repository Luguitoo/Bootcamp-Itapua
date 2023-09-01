from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from . import views

from .views import *
urlpatterns = [
    path('signup/', views.UserCreateAndLoginView.as_view(), name='signup'),
    path('login/', LoginView.as_view(redirect_authenticated_user=True, template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # ... ,
    path('user_detail/<int:pk>/', UserDetail.as_view(), name='user_detail'),
    path('user_update/<int:pk>/', UserUpdate.as_view(), name='user_update'),
    path('password_change/', PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDone.as_view(),
    name='password_change_done'),
    path('user_delete/<int:pk>/', UserDelete.as_view(), name='user_delete'),
]
