from django.shortcuts import render, redirect
from .models import Post
from django import forms
from .forms import SignUpForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={"posts":posts})

def signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'blog/signup.html', context={'form':form})
