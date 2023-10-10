from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path,include,re_path

from .views import user_login,register,logout
from dashboard import urls

urlpatterns = [
    path("register/", views.register,name='register'),
    path("login/",views.user_login  ,name='login'),
    path("mail/",views.emailsend,name='sendemail'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', include('dashboard.urls')),

    path("logout/",views.logout,name='logout'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
]