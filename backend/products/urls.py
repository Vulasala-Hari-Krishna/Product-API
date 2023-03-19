from django.urls import path
from .views import (ProductDetailAPIView, ProductCreateAPIView, ListCreateAPIView, ListAPIView,
 ProductUpdateAPIView ,ProductDestroyAPIView, ProductMixinView)

urlpatterns = [
    path('',ListCreateAPIView.as_view(),name='product-list'),
    path('list/',ListAPIView.as_view()), #ProductMixinView.as_view()), 
    path('<int:pk>/update/',ProductUpdateAPIView.as_view(), name='product-update'),
    path('<int:pk>/delete/',ProductDestroyAPIView.as_view()),
    path('create/',ProductCreateAPIView.as_view()), #ProductMixinView.as_view()), 
    path('<int:pk>/',ProductDetailAPIView.as_view(), name='product-detail') #ProductMixinView.as_view()) 
]