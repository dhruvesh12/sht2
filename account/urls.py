from django.urls import path
from account.views import *
from account import views


urlpatterns = [
    
    
    path('register/',register, name='yash'),
    path('register/sucess',sucess, name='sucess'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
   
]