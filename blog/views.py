from django.shortcuts import render, get_object_or_404, redirect
from datetime import date
from .models import Post
from .forms import CreatePostForm, LoginForm
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from .forms import LoginForm

class ListPostsView(APIView):
    def get(self, request):
        blog_posts = Post.objects.all()
        return render(request, 'templates/index.html', {'all_posts': blog_posts})

class CreatePostView(APIView):
    def get(self, request):
        form = CreatePostForm()
        return render(request, 'make-post.html', {'form': form})

    def post(self, request):
        form = CreatePostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.date = date.today().strftime('%Y-%m-%d')
            new_post.save()
            return redirect('list_posts')

        return render(request, 'make-post.html', {'form': form})

class UpdatePostView(APIView):
    def get(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        form = CreatePostForm(instance=post)
        return render(request, 'make-post.html', {'form': form, 'is_edit': True})

    def post(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        form = CreatePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('show_post', post_id=pk)

        return render(request, 'make-post.html', {'form': form, 'is_edit': True})

class DeletePostView(APIView):
    def post(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        post.delete()
        return redirect('list_posts')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('list_posts')  # Redirect to a desired page after successful login
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})



def show_post(request, post_id):
    requested_post = get_object_or_404(Post, id=post_id)
    return render(request, "post.html", {"post": requested_post})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
