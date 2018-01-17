from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy

from blog.models import *
from blog.forms import *
from django.views.generic import ListView
from django.http import HttpResponse
from django.views import generic as cbv


class UserCreateView(cbv.TemplateView):
    template_name = 'account_temp/sign_up.html'
    form_class = UserForm
    initial = {
    }

    def get_context_data(self, **kwargs):
        kwargs['form'] = UserForm()
        return super(UserCreateView, self).get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)

            login(request, authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            ))
            return HttpResponseRedirect('blog/')


class PostsListView(cbv.TemplateView):
    template_name = 'posts_list.html'
    model = PostMessage
    paginate_by = 25

    def get_context_data(self, **kwargs):
        posts = PostMessage.objects.all()
        comments = Comment.objects.all()
        try:
            context = super(PostsListView, self).get_context_data(**kwargs)
            context['post_massages'] = posts
            context['comments'] = comments
            return context
        except Http404:
            self.kwargs['page'] = 1
            context = super(PostsListView, self).get_context_data(**kwargs)
            context['post_massages'] = posts
            context['comments'] = comments
            return context


class PostCreateView(cbv.TemplateView):
    template_name = 'post_create.html'
    form_class = PostMessageForm
    initial = {
        'autor': '',
        'title': '',
        'text': '',
        'likes': 0,
        'date': datetime.now(),
    }

    def get(self, request, *args, **kwargs):
        self.user = request.user
        # self.initial['date'] = datetime.now().strftime("YYYY-MM-DD HH:MM")
        return super(PostCreateView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['autor'] = self.user.id
        kwargs['form'] = PostMessageForm()
        return super(PostCreateView, self).get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            post_massage = form.save(commit=False)
            post_massage.autor = get_object_or_404(User, pk=request.user.id)
            post_massage.date = self.initial['date']
            post_massage.save()
            return HttpResponseRedirect('blog/')


class CommentCreateView(cbv.TemplateView):
    template_name = 'add_comment.html'
    form_class = CommentForm
    initial = {
        'text': '',
        'post': '',
        'date': datetime.now(),
        'user': '',
    }

    def get(self, request, *args, **kwargs):
        self.user = request.user
        # self.initial['date'] = datetime.now().strftime("YYYY-MM-DD HH:MM")
        return super(CommentCreateView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['user'] = self.user.id
        kwargs['form'] = CommentForm()
        return super(CommentCreateView, self).get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            comment_massage = form.save(commit=False)
            comment_massage.user = get_object_or_404(User, pk=request.user.id)
            comment_massage.post = get_object_or_404(PostMessage, pk=kwargs['pk'])
            comment_massage.save()
            return HttpResponseRedirect('blog/')
