from django.urls import path
from .views import *

app_name = "users"
urlpatterns = [
    path('mypage/', mypage, name="mypage"),
    path('emoji/', emoji, name="emoji"),
    path('<str:id>/follow/', follow, name="follow"),
]
