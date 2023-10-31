from django.http import HttpResponse
from django.shortcuts import redirect, render
from CustomUser.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout


User = get_user_model()
# Create your views here.

def home(request):
    return render(request, "index.html")

def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        pass1 = request.POST['pass1']
        user = authenticate(email=email, password=pass1)
        print(user)
        if user is not None:
            if user.check_password(pass1):
                username = CustomUser.objects.get(email=email).name
                print(username)
                login(request, user)
                print(user.is_authenticated)
                return redirect(home)

    return render(request, "login.html")

def signout(request):
    logout(request=request)

    return redirect(home)

def resigner(request):
    if request.method == "POST":
        name = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']        

        if pass1 == pass2:
            UserSet = User.objects.create_user(email=email, password=pass1)
            UserSet.save()
            UserProfile = CustomUser.objects.get(email=email)
            UserProfile.name = name
            UserProfile.save()
            if UserProfile.is_active == True:
                # return HttpResponse("User Add OK")
                return redirect("signin")

    return render(request, "resigner.html") 