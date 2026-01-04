from . import views
from django.urls import path 

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('record/<int:id>/', views.record, name='record'),
    path('delete_record/<int:id>/', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:id>/', views.update_record, name='update_record'),

]
