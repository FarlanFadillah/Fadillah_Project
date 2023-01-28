from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('post', views.post, name="post"),
    path('content', views.content, name="content"),
    path('search', views.searching, name="searching"),
    path('image_upload', views.image_upload, name="image_upload"),
    path('<str:file>', views.image, name="image"),


]