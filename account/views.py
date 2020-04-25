from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages #user signup then message pass to login  page account created
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

#________________________________________________________________________________________________________Home
@login_required(login_url='login')
def account_home_view(request):
	return render(request,'account/account_home.html')

#________________________________________________________________________________________________________
def user_profile_view(request):
	userprofile = request.user.userprofile
	form = UserProfileForm(instance=userprofile)
	if request.method == 'POST':
		form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
		if form.is_valid():
			form.save()
	ctx = {'form': form}
	return render(request, 'account/userprofile.html', ctx)

#________________________________________________________________________________________________________Signup
def signup_view(request):
	if request.user.is_authenticated:
		return redirect('account-home')
	form = SignUpForm() #from
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, 'Account was created for ' + username)
			return redirect('account-home')
	return render(request,'account/signup.html',{'form': form})


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()  # load the profile instance created by the signal
#             user.profile.birth_date = form.cleaned_data.get('birth_date')
#             user.save()
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=user.username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})

#________________________________________________________________________________________________________Login
def login_view(request):
	if request.user.is_authenticated:
		return redirect('account-home')
	return render(request,'account/login.html')

#________________________________________________________________________________________________________login-check
def login_handle(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request,username=username,password=password)
		if user is not None:
			login(request, user)
			return redirect('account-home')
		else:
			messages.info(request, 'Username OR password is incorrect')
	return redirect('login')

#________________________________________________________________________________________________________Logout
def logout_view(request):
	logout(request)
	return redirect('login')
