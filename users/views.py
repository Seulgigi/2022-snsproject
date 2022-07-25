from django.shortcuts import render
from main.models import Post
from django.contrib.auth.models import User

# Create your views here.
def mypage(request):
    user = request.user
    
    posts=Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

from .models import Profile
# 해당앱의 views.py 에서 불러와서 Profile 모델을 불러오면 됨
# Create your views here.

def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    elif request.method == "POST":
        user = request.POST['user']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        res_data = {}
        if password1 != password2:
            res_data['error'] = 'differnet'
            print(res_data)
        else :
            profile = Profile(
                user = user, password1 = password1, password2 = password2,
            ) # 객체생성
            profile.save()
    return render(request, 'signup.html')