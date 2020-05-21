from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm

def index(request):
    blog = Blog.objects.order_by('-id')
    return render(request, 'blog/index.html', {'blog': blog })
def detail(request, blog_id):
    blog_text = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog/detail.html', {'blog_text': blog_text })

def add_form(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    else:
        form = BlogForm
    return render(request, 'blog/form.html', {'form': form })