from django.contrib import admin
from django.urls import path

from product_app.views import ProductAPIView, ManufacturerAPIView, CategoryAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', ProductAPIView.as_view()),
    path('products/<int:pk>/', ProductAPIView.as_view()),
    path('manufacturers/', ManufacturerAPIView.as_view()),
    path('manufacturers/<int:pk>/', ManufacturerAPIView.as_view()),
    path('categories/', CategoryAPIView.as_view()),
    path('categories/<int:pk>/', CategoryAPIView.as_view()),
]
