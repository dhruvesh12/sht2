from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_
from django.http import HttpResponseRedirect
from .models import user_extend
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required



import csv
import requests



#def register(request):
#	return render(request,'accounts/register.html')
 #Create your views here.

def sucess(request):
	return render(request,'successfull.html')

def register(request):
	if request.method == 'POST':
		u = request.POST['user']
		e = request.POST['email']
		p = request.POST['password']
		f = request.POST['first']
		l = request.POST['last']
		selected_option = request.POST.get('myCountry', None)

		User.objects.create_user(username=u,email=e,password=p,first_name=f,last_name=l)
		a=User.objects.get(username=u)
		
		
		
		#address = "kasar alley, bhave compound, bhiwandi,IN"
		api_key = "AIzaSyA2_ALSBCQ2GVBUI9OQxjJne4XBF9Zwjkw"
		api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(selected_option, api_key))
		api_response_dict = api_response.json()


		if api_response_dict['status'] == 'OK':
			latitude = api_response_dict['results'][0]['geometry']['location']['lat']
			longitude = api_response_dict['results'][0]['geometry']['location']['lng']
			user_extend.objects.create(latitde=latitude,longitude=longitude,user_name=a)
	
		
		return HttpResponseRedirect('/register/sucess')
	return render(request, 'accounts/register.html',{})
	

def login(request):
	if request.method =='POST':

		us=request.POST['user_']
		pas=request.POST['password']
		user = authenticate(request, username=us,password=pas)
		if user is not None:
			login_(request, user)
			return redirect("/")			
			#return render(request, 'accounts/login.html',{})
		else:
			return HttpResponse("sorry")
	return render(request, 'accounts/login.html',{})
	


@login_required
def logout(request):
    
    django_logout(request)

    return redirect('/')