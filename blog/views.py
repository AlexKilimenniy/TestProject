from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from blog.models import *
from blog.forms import *


def BlogHome(request):
    return redirect(BlogHomePage)


@login_required(login_url='/login/')
def BlogHomePage(request):
    posts = PostMessage.objects.all()
    comments = Comment.objects.all()
    return render(request, 'posts_list.html', {'post_massages': posts, 'comments': comments})


def BlogSignUp(request):
    user_form = UserForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)

            login(request, authenticate(
                username=user_form.cleaned_data['username'],
                password=user_form.cleaned_data['password']
            ))
        return redirect(BlogHomePage)
    return render(request, 'login/sign_up.html', {'user_form': user_form, })


@login_required(login_url='/login/')
def CreatePost(request):
    post_form = PostMessageForm()
    if request.method == 'POST':
        post_form = PostMessageForm(request.POST)
        if post_form.is_valid():
            post_massage = post_form.save(commit=False)
            post_massage.post_user = get_object_or_404(User, pk=request.user.id)
            post_massage.save()
            return redirect(BlogHomePage)

    return render(request,  'post_create.html', {'post_form': post_form, })


def CreateComment(request, pk):
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_massage = comment_form.save(commit=False)
            comment_massage.comment_user = get_object_or_404(User, pk=request.user.id)
            comment_massage.comment_post = get_object_or_404(PostMessage, pk=pk)
            comment_massage.save()
            return redirect(BlogHomePage)

    return render(request,  'add_comment.html', {'post_form': comment_form, })