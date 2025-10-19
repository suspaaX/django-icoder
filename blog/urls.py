from django.urls import path ,include
from .import views

urlpatterns = [
    
    path('postComment',views.postComment, name= 'postCommnet') ,
    path('', views.blogHome, name='blogHome'),
    path('<str:slug>', views.blogPost, name='blogPost'),

]