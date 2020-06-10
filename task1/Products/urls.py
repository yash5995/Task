from django.urls import path
from . import views
urlpatterns = [

path('', views.page),
    path('product/',views.fetch_product,name='product'),
    path('update_post/',views.update_product,name='updated_product'),
]