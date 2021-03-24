from django.urls import path
from . import views



urlpatterns = [
    path('', views.Testmony_list.as_view(), name='testimony'),
    path('review', views.testmony, name='writereview')
]
