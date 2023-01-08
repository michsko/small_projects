from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			# Redirect to a success page.
			return redirect ('home')
		else:
			# Return an 'invalid login' error messages.
			messages.success(request, ('There is a problem with your login.'))
			return  redirect('login_user')

	else:
		return render(request, 'authenticate/login.html', {})




def logout_user(request):

	logout(request)
	messages.success(request, ('You were logout. '))
	return redirect('home')