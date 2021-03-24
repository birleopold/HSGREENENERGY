from django.urls import path
from . import views



urlpatterns = [
    path('', views.project_list, name='projects'),
    path('<int:pk>/', views.Project_detail.as_view(), name='project_detail'),
]
