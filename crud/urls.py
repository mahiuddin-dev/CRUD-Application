from django.urls import path
from . import views

app_name = 'crud'

urlpatterns = [
    path('', views.index, name='index'),
    path('leads/create/', views.leads_create, name='leads_create'),
    path('leads/search/', views.search, name='search'),
    path('leads/<pk>/update/', views.leads_update, name='leads_update'),
    path('leads/<pk>/delete/', views.leads_delete, name='leads_delete'),
]
