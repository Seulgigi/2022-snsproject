from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', showmain, name="showmain"),
    path('firstpage/', firstpage, name="firstpage"),
    path('<str:id>', detail, name="detail"),
    path('life/<str:id>', lifedetail, name="lifedetail"),
    path('new/', new, name="new"),
    path('life/new/', lifenew, name="lifenew"),
    path('create/', create, name="create"),
    path('life/create/', lifecreate, name="lifecreate"),
    path('posts/', posts, name="posts"),
    path('life/posts/', lifeposts, name="lifeposts"),
    path('edit/<str:id>', edit, name="edit"),
    path('life/edit/<str:id>', lifeedit, name="lifeedit"),
    path('update/<str:id>', update, name="update"),
    path('life/update/<str:id>', lifeupdate, name="lifeupdate"),
    path('delete/<str:id>', delete, name="delete"),
    path('life/delete/<str:id>', lifedelete, name="lifedelete"),
    path('<str:post_id>/create_comment', create_comment, name="create_comment"),
    path('<str:comment_id>/update_comment', update_comment, name="update_comment"),
    path('<str:comment_id>/delete_comment', delete_comment, name="delete_comment"),
    path('<str:comment_id>/edit_comment', edit_comment, name="edit_comment"),
    path('like_toggle/<str:post_id>/', like_toggle, name="like_toggle"),
    path('my_like/<str:user_id>', my_like, name='my_like'),
]