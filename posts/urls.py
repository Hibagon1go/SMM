from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views
from posts.views import PostDetailView, TagListView, Law_Politics_View, Medical_View, Engineering_View, Society_View, Science_View, Agriculture_View, Economics_View, Education_View, Liberal_Arts_View, Nongenre_View, SearchPostView #CategoryListView

app_name = 'posts'

urlpatterns = [
    path('new/', login_required(views.New.as_view()), name='new'),
    path('', login_required(views.Index.as_view()), name='index'),
    path('all/', login_required(views.All.as_view()), name='all'),
    path('search_post/', login_required(SearchPostView.as_view()), name='search_post'),
    path('law_politics/', login_required(Law_Politics_View.as_view()), name='law_politics'),
    path('medical/', login_required(Medical_View.as_view()), name='medical'),
    path('engineering/', login_required(Engineering_View.as_view()), name='engineering'),
    path('society/', login_required(Society_View.as_view()), name='society'),
    path('science/', login_required(Science_View.as_view()), name='science'),
    path('agriculture/', login_required(Agriculture_View.as_view()), name='agriculture'),
    path('economics/', login_required(Economics_View.as_view()), name='economics'),    
    path('education/', login_required(Education_View.as_view()), name='education'),
    path('liberal_arts/', login_required(Liberal_Arts_View.as_view()), name='liberal_arts'),  
    path('nongenre/', login_required(Nongenre_View.as_view()), name='nongenre'),      
    path('<postId>/like/', login_required(views.Likes.as_view()), name='like'),
    path('<postId>/comment/', login_required(views.AddComment.as_view()),name='comment'), 
    path('<postId>/', PostDetailView.as_view(), name='post_detail'),
    #path('categories/', CategoryListView.as_view(), name='category_list'),
    path('tags/', TagListView.as_view(), name='tag_list'),  

]
