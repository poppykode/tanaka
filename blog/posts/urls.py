from django.urls import path
from .views import (
    about_us as ab, 
    home, post_details,
    create_post
) 

app_name = 'posts'
urlpatterns = [
    path('',home, name='home'),
    path('about',ab, name='about'),
    path('post-details/<int:id>',post_details, name='post_details'),
    path('create-post',create_post,name='create_post')

]