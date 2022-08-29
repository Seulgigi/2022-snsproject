from django.urls import path
from .views import *

app_name = "users"
urlpatterns = [
    path('<str:id>/mypage/', mypage, name="mypage"),
    path('<str:id>/emoji/', emoji, name="emoji"),
    path('<str:id>/follow/', follow, name="follow"),
]
