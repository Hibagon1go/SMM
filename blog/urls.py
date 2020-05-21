
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
        path('', views.index, name='index'),
        path('detail/<int:blog_id>/', views.detail, name='detail'),
         path('add_form', views.add_form, name='add_form'), 
]