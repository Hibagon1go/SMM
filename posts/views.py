from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views import  View

from .forms import PostForm
from .models import Post,Like,Comment
from accounts.models import User #added




class New(CreateView):
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:index')

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super(New, self).form_valid(form)

class Index(ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 100
    queryset = Post.objects.order_by('created_at').reverse()

    def get_context_data(self, **kwargs):
        user = self.request.user #added
        followees = list(user.followees.all()) #added
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





    



