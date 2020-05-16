from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views import  View
from django.db import models
from django.db.models import Count, Q
from django.http import Http404
from django.views.generic.detail import DetailView

from .forms import PostForm
from .models import Post,Like,Comment,Category,Tag
from accounts.models import User #added




class New(CreateView):
    template_name = 'posts/new.html'
    form_class = PostForm

    def form_valid(self, request):
        if self.request.method == "POST":
            form = PostForm(self.request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = self.request.user
                post.save()
                return redirect('posts:index')
        else:
            form = PostForm()
        
        return render(request, 'posts/index.html', {'form': form})
            

class Index(ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 100
    queryset = Post.objects.order_by('created_at').reverse()

    def get_context_data(self, **kwargs):
        user = self.request.user 
        followees = list(user.followees.all())
        followees.append(user)
        context = {}
        like_list = {}
        comment_list = {}
        likes_total = {}
        Post_lst = []   
        context['post_list']=Post.objects.filter(author__in=followees).order_by('created_at').reverse()
        for post in context['post_list']: 
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
            'user' : self.request.user,
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
            'user' : self.request.user,
            'like_list': like_list,
            'comment_list': comment_list,
            'likes_total' : likes_total,
            'post': post
        })

class All(ListView):
    model = Post
    template_name = 'posts/all.html'
    paginate_by = 100
    queryset = Post.objects.order_by('created_at').reverse()

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        user = self.request.user #added
        followees = user.followees.all() #added
        like_list = {}
        comment_list = {}
        likes_total = {}
        Post_lst = []   
        for post in context['post_list']:
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

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    slug_field = 'post'
    slug_url_kwarg = 'postId'

    def get(self, request, postId):
        post = Post.objects.get(id=postId)
        return render(request, 'posts/post_detail.html', {
            'post': post
        })


class CategoryListView(ListView):
    queryset = Category.objects.annotate(
        num_posts=Count('post', filter=Q(post__is_public=True)))


class TagListView(ListView):
    queryset = Tag.objects.annotate(num_posts=Count(
        'post', filter=Q(post__is_public=True)))



    



