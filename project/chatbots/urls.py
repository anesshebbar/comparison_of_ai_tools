from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('novels/', views.novel_list, name='novel_list'),
    path('novel/<int:novel_id>/', views.novel_detail, name='novel_detail'),
    path('novel/<int:novel_id>/review/', views.add_review, name='add_review'),
    path('logout/', views.logout_request, name='logout'),
    path('register/', views.register, name='register'),
]