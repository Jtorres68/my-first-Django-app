from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),    #the name is the name of the URL that will be used to identify the view
    path('post/<int:pk>/', views.post_detail, name='post_detail'), #post/<int:pk>/ specifies a URL pattern such as http://127.0.0.1:8000/post/1/
]