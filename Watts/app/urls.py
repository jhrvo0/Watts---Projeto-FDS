from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.HomeViews.as_view(), name ='home'),
    path('addLocacao/', views.AddLocacao.as_view(), name = 'addLocacao'),
    path('addComodo/', views.AddComodo.as_view(), name = 'addComodo'),
]
