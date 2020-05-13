from django.shortcuts import render, get_object_or_404, redirect #後者二つadded
from django.views import generic,View #後者added
from django.urls import reverse 
from django.views.generic import ListView #added
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth import login

from .forms import SignUpForm
from .models import User
from posts.models import Post,Like,Comment #added


from django.contrib import messages #added
from django.views.decorators.http import require_POST#added
from django.contrib.auth.decorators import login_required #added

# サインアップ画面
class SignUpView(generic.CreateView):
    # 使うformクラス設定
    form_class = SignUpForm
    # 使うテンプレートファイル設定
    template_name = 'registration/signup.html'

    # 成功時にログイン処理を行ってAccountDetailViewに飛ぶ
    def get_success_url(self):
        form = self.get_form()
        # usernameから登録したユーザー情報を参照
        user = User.objects.get(username=form.data.get('username'))

        # ログイン処理を行う
        login(self.request, user)
        return reverse(
            'accounts:userDetail',
            kwargs={'username': user.username })


class AccountDetailView(DetailView):
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'

    # 以下関数を新規追加 テンプレートにわたすデータにログイン中ユーザーの情報も追加する
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['login_user'] = self.request.user
        return context

# 以下のコードを追加
class IconEdit(UpdateView):
    model = User
    template_name = 'accounts/icon_edit.html'
    fields = ['icon']

    def get_object(self):
        # ログイン中のユーザーで検索することを明示する
        return self.request.user

    def get_success_url(self):
        form = self.get_form()
        return reverse(
            'accounts:userDetail',
            kwargs={'username': self.request.user.username})

class UserFollowView(View): #added
    model = User
    template_name = 'accounts/user_detail.html'
    
    #@require_POST
    def user_follow(self, request):
        login_user = request.user
        user = User.objects.get(username=user.username) #added ここは今いるページのユーザーの情報を取りたい
        followees = login_user.followees.all() #added
        #今見ているページの人が既にフォローしていれば解除、していなければフォロー
        if user in followees:
            login_user.followees.remove(user)
            return messages.success(request, 'フォローを解除しました')
        else:
            login_user.followees.add(user)
            return messages.success(request, 'フォローしました')

        return reverse(
            'accounts:userDetail',
            kwargs={'username': user.username})


class FollowListView(ListView):#added
    model = User
    template_name = 'accounts/followlist.html'

    def users_followlist(self, request): 
        user = user
        #その人がフォローしているユーザー
        followees = user.followees.all()
        #その人をフォローしているユーザー
        followers = User.objects.filter(followees=user)
        context = {
            'user': user,
            'followees': followees,
            'followers': followers,
        }
        return render(request, 'accounts/followlist.html', context)    

class MyPostView(ListView): #added
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 100
    queryset = Post.objects.order_by('created_at').reverse()

    def get_context_data(self, **kwargs):
        Context = super().get_context_data()
        user = self.request.user #added
        like_list = {}
        comment_list = {}
        likes_total = {}
        Post_lst = []   
        context = {}  
        for post in Context['post_list']: 
            if post.author == user:
                context['post_list'] = Post.objects.filter(id=post.id)
                Post_lst.append([post.id,post])

        for i in Post_lst:
            like_list[i[0]] = Like.objects.filter(post=i[1])
            comment_list[i[0]] = Comment.objects.filter(post=i[1])  
            likes_total[i[0]] = len(Like.objects.filter(post=i[1])) #added
        context['username'] = user.username
        context['like_list'] = like_list
        context['likes_total'] = likes_total #added
        context['comment_list'] = comment_list  
        return context


class Likes(View):
    model = Like
    slug_field = 'post'
    slug_url_kwarg = 'postId'

    def get(self, request, postId):
        post = Post.objects.get(id=postId)
        like = Like.objects.filter(author=self.request.user, post=post)
        like_list = {}
        comment_list = {}  
        likes_total = {} #added
        if like.exists():
            like.delete()
        else:
            like = Like(author=self.request.user, post=post)
            like.save()
        like_list[post.id] = Like.objects.filter(post=post)
        comment_list[post.id] = Comment.objects.filter(post=post) 
        likes_total[post.id] = len(Like.objects.filter(post=post)) #added
        return render(request, 'posts/like.html', {
            'like_list': like_list,
            'comment_list': comment_list,  
            'likes_total' : likes_total, #added
            'post': post
        })


class AddComment(View):
    def post(self, request, postId):
        like_list = {}
        comment_list = {}
        likes_total = {} #added

        post = Post.objects.get(id=postId)
        text = request.POST["comment"]

        comment = Comment(author=self.request.user, post=post, text=text)
        comment.save()

        like_list[post.id] = Like.objects.filter(post=post)
        comment_list[post.id] = Comment.objects.filter(post=post)
        likes_total[post.id] = len(Like.objects.filter(post=post)) #added
        
        return render(request, 'posts/like.html', {
            'like_list': like_list,
            'comment_list': comment_list,
            'likes_total' : likes_total,
            'post': post
        })

