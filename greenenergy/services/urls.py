from django.urls import path
from . import views


urlpatterns = [
    path('', views.service_list, name='services'),
    path('<int:pk>/', views.Service_detail.as_view(), name='service_detail'),
]
