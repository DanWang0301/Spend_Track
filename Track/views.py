from django.shortcuts import render, redirect
from Track.models import *
from .forms import *

# def display(request):
#     post = TrackType.objects.filter(User_Email=CustomUser.objects.get(email=str(request.user)))
#     # print("email:", request.user)
#     return render(request, "track_page/track_detail.html", post)



class TrackTypeView():
    def insert(request):
        post = TrackType.objects.filter(User_Email=CustomUser.objects.get(email=str(request.user)))

        form = TrackTypeModelForm()
        if request.method == "POST":
            form = TrackTypeModelForm(request.POST, user=request.user)
            if form.is_valid():
                track_type = form.save(commit=False)
                track_type.User_Email = request.user  # 设置外键字段
                track_type.save()
                return redirect('/tracktype_setting')
        else:
            form = TrackTypeModelForm(user=request.user)

        context = {
                'form': form,
                'post': post
            }
        return render(request, 'track_page/track_type/track_type_setting.html', context)

class TrackRecordView():
    def insert(request):
        post = TrackRecord.objects.filter(User_Email=CustomUser.objects.get(email=str(request.user)))

        form = TrackRecordModelForm()
        if request.method == "POST":
            form = TrackRecordModelForm(request.POST, user=request.user)
            if form.is_valid():
                track_record = form.save(commit=False)
                track_record.User_Email = request.user  # 设置外键字段
                track_record.save()
                return redirect('/track_record')
        else:
            form = TrackRecordModelForm(user=request.user)

        context = {
                'form': form,
                'post': post
            }
        return render(request, 'track_page/track_record/track_record.html', context)

    def update(request):
        if request.method == 'POST':
            Track_Type = request.Post['Track_Type']
            Credit_Card = request.Post['Spend_Type']
            Track_Amount = request.Post['Amount']
            Track_Detail = request.Post['Detail']
            Track_Date = request.Post['Date']

def select(request):
    pass

def delete(request):
    if request.method == 'POST':
        Track_Type = request.Post['Track_Type']
        Credit_Card = request.Post['Spend_Type']
        Track_Amount = request.Post['Amount']
        Track_Detail = request.Post['Detail']
        Track_Date = request.Post['Date']