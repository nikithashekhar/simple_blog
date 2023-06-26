from django.urls import path
from . import views
from .views import HomeView, DeetView, AddPost, EditPost, DeletePost, AddCat, AddCatView, AddCatListView, LikeView, AddComment


urlpatterns = [
    # path('', views.home, name = "home"),
    path('', HomeView.as_view(), name = "home"),
    path('article/<int:pk>', DeetView.as_view(), name = "article_view"),
    path('addBlog/', AddPost.as_view(), name = "addBlog"),
    path('addCategory/', AddCat.as_view(), name = "addCat"),
    path('article/edit/<int:pk>', EditPost.as_view(), name = "edit_post"),
    path('article/<int:pk>/remove', DeletePost.as_view(), name = "delete_post"),
    path('category/<str:cat>/', AddCatView, name = "category"),
    path('category-list/', AddCatListView, name = "category-list"),
    path('like/<int:pk>', LikeView, name = "like_post"),
    path('article/<int:pk>/comment/', AddComment.as_view(), name = "addComment"),
]