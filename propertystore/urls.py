from django.urls import path
from . import views
from dashboard import views as viewss

urlpatterns = [
    path('', views.store, name='store'),
    path('category/<slug:category_slug>/', views.store, name='property_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.property_detail, name='property_detail'),
    path('search/', views.search, name='search'),
    path('message/<int:id>/', viewss.messagefrombuyer, name='messagefrombuyer'),
    path('search', views.search, name='search'),


]