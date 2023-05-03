from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('manage_polls/', views.manage_polls, name='manage_polls'),
    path('create_poll/', views.create_poll, name='create_poll'),
    path('view_results/<int:poll_id>/', views.view_results, name='view_results'),
]
