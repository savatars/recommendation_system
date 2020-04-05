from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from mysite.models import features
from django.views.decorators.csrf import csrf_exempt
import math
import json
from scipy import spatial
feature_set=[]
for i in (features.objects.all()):
	feature_set.append(list(map(int,i.recommendedProducts.split(","))))


# Create your views here.
def register(request):
		if request.method=="POST":
			form=UserRegisterForm(request.POST)
			if form.is_valid():
				form.save()
				username=form.cleaned_data.get('username')
				messages.success(request,f'your account has been created! you are now able to login')
				return redirect('login')
		else:
			form=UserRegisterForm()	
		return render(request,'users/register.html',{'form':form})
  
@login_required	
@csrf_exempt
def profile(request):
	products=[420,88,776,1123,4,987,55,4523,9987,69]
	prod_input=products
	
	if request.method == 'POST':
		result=[]
		count =0
		prod_input=request.POST.get('data')
		print(type(prod_input))
		'''
		prod_input=list(map(int,prod_input))
		for i in range(1,99):
			result1= 1 - spatial.distance.cosine(prod_input,feature_set[i])
			result.append(result1)
			count=count+1
			index_min=result.index(min(result))
			products=feature_set[index_min]
			'''
		k=[233,32323,23,233,556,5,7,575,64,3]
		print('allah')
		k=json.dumps({'k':k})
		return HttpResponse(k)
	return render(request,'users/main.html',{'products':products})