from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Count, Q
from django.core.paginator import Paginator
from .models import Post, Comment, Like
from .forms import PostForm


def home_page(request):
    query = request.GET.get('q', '')
    posts = Post.objects.all()
    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(content__icontains=query)).distinct()
    posts = posts.annotate(like_count=Count('likes'), comment_count=Count('comments'))
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'posts': page_obj, 'query': query})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    post.views_count += 1
    post.save(update_fields=['views_count'])
    comments = post.comments.all()
    user_liked = False
    if request.user.is_authenticated:
        user_liked = Like.objects.filter(post=post, user=request.user).exists()
    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'user_liked': user_liked,
    })


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form, 'form_type': 'Yangi'})


@login_required
def update_post(request, id):
    post = get_object_or_404(Post, id=id, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_form.html', {'form': form, 'form_type': 'Tahrirlash'})


@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('home_page')
    return render(request, 'post_confirm_delete.html', {'post': post})


@login_required
def add_comment(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Comment.objects.create(post=post, user=request.user, text=text)
    return redirect('post_detail', id=post.id)


@login_required
def like_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        like, created = Like.objects.get_or_create(post=post, user=request.user)
        if not created:
            like.delete()
    return redirect('post_detail', id=post.id)


def profile(request, username):
    from django.contrib.auth.models import User
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user)
    total_likes = Like.objects.filter(post__author=user).count()
    return render(request, 'profile.html', {
        'profile_user': user,
        'posts': posts,
        'total_likes': total_likes,
    })


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home_page')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
