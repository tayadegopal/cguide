from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('viewProfile/<int:id>',views.viewProfile,name='viewProfile'),
    path('post/',views.postPage,name='post'),
    path('likePost/',views.likePost,name="likePost"),
    path('comment/<int:id>',views.commentPost,name="comment"),
    path('editProfile/<int:id>',views.editProfile,name="editProfile"),
    path('dashboard/',views.dashboard,name="dashboard"),


]