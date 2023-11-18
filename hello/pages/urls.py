from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='url_index'),
    path('<int:geturl>/', views.getchislo),
    path('<str:geturl>/', views.geturl, name='url_page_name'),
    ]