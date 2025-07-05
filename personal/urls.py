from django.urls import path
from personal import views

urlpatterns = [
    path('', views.index_view, name='index'),
]
