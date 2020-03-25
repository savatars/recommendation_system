from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
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
	if request.method=='POST':

		prod_input=request.POST.get('data')
		print(prod_input)
	return render(request,'users/main.html',{'products':products})

@csrf_exempt
def final(request):
	products=[420,88,776,1123,4,987,55,4523,9987,69]
	prod_input=request.POST.get('product_list')
	print('allah')
	print(prod_input)
	return render(request,'users/main.html',{'products':products})