from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('product/<str:pk>', views.product, name='product'),
    path('category_summary/', views.category_summary, name='category_summary'),
    path('category<str:word>/', views.category, name='category'),
    path('search/', views.search, name='search'),
    path('upload_product/', views.upload_product, name='upload_product'),
    path('edit_product/<str:pk>', views.edit_product, name='edit_product'),
    path('add_category/', views.add_category, name='add_category'),
    path('edit_category<str:word>/', views.edit_category, name='edit_category'),
]


