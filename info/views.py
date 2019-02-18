from django.shortcuts import render,HttpResponse,get_object_or_404,render_to_response
from info.models import *
from django.contrib.auth.models import User
from django.contrib.auth import logout



def forms(request):
	if request.method== 'POST':
		f=request.POST['head']
		m=request.POST['mid']
		l=request.POST['la']
		c_id=request.POST['cats']
		c=category.objects.get(id=c_id)
		imgs = request.FILES['img']

		a=request.user

		infy.objects.create(name=f,middle=m,last=l,category=c,img=imgs,first=a)


		

	other=category.objects.all()
	return render(request,'forms.html',{'other':other})


def bridal_detail(request,pk):
	a = get_object_or_404(infy, pk=pk)
	b = userImage.objects.filter(user=request.user)


	
	#b = get_object_or_404(userImage, pk=pk)
	return render(request,'bride_detail.html',{'a':a,'b':b})


def bridels_list(request):
	post=infy.objects.all()
	return render(request,'bride.html',{'post':post})


def category_list(request,pk):
	
	a = infy.objects.filter(category=pk)
	
	return render(request,'bride_search.html', {'a':a})


def upload_img(request):
	limit=2621440

	if request.method == 'POST':
		imgs = request.FILES.getlist('img')
		a=request.user
		for img in imgs:
			if img.size < limit:
				u = userImage.objects.create(img=img,user=a)
				u.save()
			else:
				return HttpResponse('upload not supported')

		return HttpResponse("hdj")

	return render(request, 'multiple_img.html')





def home_page(request):
#    if request.GET:
#        search_term = request.GET['search']
#        results = infy.objects.filter(name__istartswith=search_term)
	post=category.objects.all()
	a=User.objects.all()
	
	
#        return render_to_response('home.html', {'results': results,'post':post})
	return render(request,'home.html', {'post':post,'a':a})



def dashboard(request,pk):
	dash=get_object_or_404(User, pk=pk)

	return render(request,'dashboard.html',{'dash':dash})

# Create your views here.


