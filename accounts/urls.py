from django.urls import path
from . import views
app_name= 'accounts'

urlpatterns = [
    path('<username>/mypost', views.MyPostView.as_view(), name='mypost') ,
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('<username>/', views.AccountDetailView.as_view(), name='userDetail'),
    path('icon/edit/', views.IconEdit.as_view(), name='icon_edit'),
    path('<username>/follow', views.UserFollowView.as_view(),name='follow'), #added
    path('<username>/followlist', views.FollowListView.as_view(),name='followlist'), #added
]