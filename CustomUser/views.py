from django.http import HttpResponse
from django.shortcuts import redirect, render
from CustomUser.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from Track.models import TrackType


User = get_user_model()
# Create your views here.

def home(request):
    return render(request, "index.html")

def signin(request):
    if request.user.is_authenticated:
        return redirect(home)

    if request.method == 'POST':
        email = request.POST['email']
        pass1 = request.POST['pass1']
        user = authenticate(email=email, password=pass1)
        if user is not None:
            if user.check_password(pass1):
                # username = CustomUser.objects.get(email=email).name
                # print(username)
                login(request, user)
                # print(user.is_authenticated)
                return redirect(home)
            else:
                return render(request, "authentication_page/login.html", {"wrong_password":True})

        else:
            return render(request, "authentication_page/login.html", {"wrong_user":email})

    return render(request, "authentication_page/login.html")

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

            # UserTrackType_create = [
            #     TrackType(User_Email = UserProfile, Spend_Type = "Pay in Cash(付現)"),
            #     TrackType(User_Email = UserProfile, Spend_Type = "Credit Card(信用卡)")
            # ]
            # TrackType.objects.bulk_create(UserTrackType_create)
            if UserProfile.is_active == True:
                return redirect("signin")

    return render(request, "authentication_page/resigner.html") 