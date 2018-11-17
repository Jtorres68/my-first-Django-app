from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),    #the name is the name of the URL that will be used to identify the view
    path('post/<int:pk>/', views.post_detail, name='post_detail'), #post/<int:pk>/ specifies a URL pattern such as http://127.0.0.1:8000/post/1/
    path('post/new/', views.post_new, name='post_new'),  #url path to add new post
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'), #url path to edit currently existing file
    path('post/<pk>/remove', views.post_delete, name='post_delete'), #url path to remove a post
    path(r'^post/(?P<pk>\d+)/comment/$', views.add_message, name='add_message'), #url path for consumer to send a message
    path('post/Thank_you', views.Thank_you, name='Thank_you'), #Thank you message after sending interest
    path('', views.product_state, name='product_state'),
]