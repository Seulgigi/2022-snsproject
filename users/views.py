from django.shortcuts import get_object_or_404, redirect, render
from matplotlib.style import context
from main.models import Post
from .models import *
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView

# Create your views here.
def mypage(request, id):
    user = get_object_or_404(User, pk = id)

    context={
        'user':user,
        'posts':Post.objects.filter(writer=user),
        'followings':user.profile.followings.all(),
        'followers':user.profile.followers.all(),
    }
    
    posts=Post.objects.filter(writer=user)
    return render(request,'users/mypage.html', context)

class ProfileView(DetailView):
    context_object_name = 'profile_user' # model로 지정해준 User모델에 대한 객체와 로그인한 사용자랑 명칭이 겹쳐버리기 때문에 이를 지정해줌.
    model = User
    template_name = 'kilogram/profile.html'

from .models import Profile
# 해당앱의 views.py 에서 불러와서 Profile 모델을 불러오면 됨
# Create your views here.

def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    elif request.method == "POST":
        user = request.POST['user']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        res_data = {}
        if password1 != password2:
            res_data['error'] = 'differnet'
            print(res_data)
        else :
            profile = Profile(
                user = user, email=email, password1 = password1, password2 = password2,
            ) # 객체생성
            profile.save()
    return render(request, 'signup.html')

def emoji(request, id):
    # user = request.user
    # user = get_object_or_404(User, pk=id)

    if request.method == "POST":
        profile = Profile.objects.get(user=request.user, pk=id)
        profile.img = request.FILES.get('img')
        profile.save(update_fields=['img'])
    return redirect('users:mypage', profile.id)


def follow(request, id):
    user = request.user
    followed_user = get_object_or_404(User, pk=id)
    is_follower = user.profile in followed_user.profile.followers.all()
    if is_follower:
        user.profile.followings.remove(followed_user.profile)
    else:
        user.profile.followings.add(followed_user.profile)
    return redirect('users:mypage', followed_user.id)