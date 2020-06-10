from django.urls import path
from . import views
urlpatterns = [

path('', views.index, name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.register,name='login'),
    path('post/',views.check_user,name='post'),
    path('post_submit/',views.post_get,name='post_submit'),
    path('update/',views.updated_post,name='updated_post'),
    ]