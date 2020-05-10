from django.urls import path
from . import views
app_name= 'accounts'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('<username>/', views.AccountDetailView.as_view(), name='userDetail'),
    path('icon/edit/', views.IconEdit.as_view(), name='icon_edit'),
    path('follow', views.UserFollowView.as_view(),name='follow'), #added
    path('followlist', views.FollowListView.as_view(),name='followlist'), #added
    path('mypost', views.MyPostView.as_view(), name='mypost') #added
]