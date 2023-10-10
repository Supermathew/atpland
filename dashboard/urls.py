from django.contrib import admin
from django.urls import path
from . import views
# from django.urls import path,include,re_path

# from .views import user_login,register,logout

urlpatterns = [
    
    path('', views.dashboard  ,name='dashboard'),
    path('wishlist/', views.wishlist  ,name='wishlist'),
    path('upload/', views.upload  ,name='upload'),
    path('message/', views.message  ,name='message'),
    path('verify/', views.verify  ,name='verify'),
    path('changepassword/', views.changepassword  ,name='changepassword'),
    path('logout/', views.logout  ,name='logout'),
    path('setpassword/', views.setpassword  ,name='setpassword'),
    path('Yourproperty/', views.Yourproperty  ,name='Yourproperty'),
    path('detailsupdate/<slug:product_slug>/', views.property_update  ,name='property_update'),
    path('verify/<int:pk>/', views.verify  ,name='profileupdate'),
    path('propertydelete/<slug:product_slug>/', views.property_delete  ,name='propertydelete'),


    









]