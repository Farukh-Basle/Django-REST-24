from django.urls import path,include
from FBVapp import views

urlpatterns = [
    path('products/',views.ProductListView),
    path('products/<int:pk>',views.ProductDetailView),
]