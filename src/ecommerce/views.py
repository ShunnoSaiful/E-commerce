from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User 
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm

def home_page(request):
	return render(request, "index.html", {})

def about(request):
	return render(request, "about.html", {})
def blog(request):
	return render(request, "blog.html", {})

def cart(request):
	return render(request, "cart.html", {})

def category(request):
	return render(request, "category.html", {})

def checkout(request):
	return render(request, "checkout.html", {})

def confirmation(request):
	return render(request, "confirmation.html", {})

def contact(request):
	return render(request, "contact.html", {})

def elements(request):
	return render(request, "elements.html", {})

def single_blog(request):
	return render(request, "single-blog.html", {})

def single_product(request):
	return render(request, "single-product.html", {})

def tracking(request):
	return render(request, "tracking.html", {})




def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
		'form':form
	}
	print("User logged in")
	print(request.user.is_authenticated)
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(request, username=username, password=password)
		print(request.user.is_authenticated)
		if user is not None:
			login(request, user)
			print(request.user.is_authenticated)
			# Redirect to a success page.
			# context['form'] = LoginForm()
			return redirect('/')
		else:
			...
	return render(request, "login.html", context)



def register_page(request):
	form = RegisterForm(request.POST or None)
	context = {
		"form":form
	}
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
		new_user = User.objects.create_user(username,email,password)
		print(new_user)
	return render(request, "register.html", context)