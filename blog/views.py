<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def blog_home(request, posts=None):
    if posts:
        post_list = posts
    else:
        post_list = Post.objects.order_by('-date_posted').all()

    paginator = Paginator(post_list, 4) # 한 페이지에 8개씩 표시
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}

    return render(request, 'blog/home.html', context)

@login_required
def blog_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "새로운 글이 등록되었습니다.")
            return redirect('blog-home')
    else:
        form = PostForm()
    return render(request, 'blog/create.html', {'form': form})

@login_required
def blog_update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "글이 수정되었습니다.")
            return redirect('blog-home')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/update.html', {'form': form})

@login_required
def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/detail.html', {'post': post})

@login_required
def blog_user_posts(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user).order_by('-date_posted')

    paginator = Paginator(posts, 4) # 한 페이지에 8개씩 표시
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, 'username': user.username}
    
    return render(request, 'blog/user_posts.html', context)

@login_required
def blog_delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        messages.success(request, "글이 삭제되었습니다.")
        post.delete()
        return redirect('blog-home')
    else:
        return render(request, 'blog/delete.html', {'post': post})



def index(request):
=======
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
    )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "글이 수정되었습니다.")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'There was an error in your submission.')
        return super().form_invalid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/blog/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
def blog_home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)

def blog_create(request):
    user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "새로운 글이 등록되었습니다.")
            return redirect('blog-home')
    else:
        form = PostForm()
    return render(request, 'blog/create.html', {'form': form})

def blog_update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "글이 수정되었습니다.")
            return redirect('blog-home')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/update.html', {'form': form})

def blog_delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        messages.success(request, "글이 삭제되었습니다.")
        post.delete()
        return redirect('blog-home')
    else:
        return render(request, 'blog/delete.html', {'post': post})



def index(request):
>>>>>>> 5cfd106dbc2f54bb5d33a8ff7acb54b2c0160108
    return render(request, 'index.html')