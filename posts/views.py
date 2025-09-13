from django.shortcuts import redirect, render
from .models import Post
from django.contrib.auth.decorators import login_required
from. import forms

def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': posts})

def post_page(request, pk, slug):
    post = Post.objects.get(pk=pk)
    return render(request, 'posts/post_page.html', {'post': post})

@login_required(login_url="/users/login/") # decorator checa se tá logado. Se não, ele redireciona para o login_url
def post_new(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post_new.html', {'form': form})

def post_update(request, pk, slug):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:page', pk=post.pk, slug=post.slug)
    else:
        form = forms.CreatePost(instance=post)
    
    context = {
        'form': form,
        'post': post
    }
    return render(request, 'posts/post_update.html', context)

def post_delete(request, pk, slug):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
    return redirect('posts:list')