from django.urls import path
from info.views import *
from info import views


urlpatterns = [
	path('',home_page,name='home_page'),
	path('dash/<int:pk>/',dashboard,name='dashboard'),
	path('dash/img/',upload_img,name='upload_img'),
	path('search/<int:pk>/',category_list,name='category_list'),
	path('bride/',bridels_list,name='bridels_list'),
	path('forms/',forms,name='forms'),
	path('bride/<int:pk>/',bridal_detail,name='bridal_detail'),


]