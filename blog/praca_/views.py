from django.shortcuts import render
from django.http import HttpResponse
from .models import Page, Post, Literature
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView



def hello(request):
    return HttpResponse("Hello")


def page_view(request):
    context = {}
    context["all_pages"] = Page.objects.all()
    return render(request, "all_pages_func.html", context)


class PageListView(ListView):
    model = Page
    template_name = "all_pages_class.html"

class Page_ListView(ListView):
    model = Post
    template_name = "all_posts_class.html"

class PageCreateView(CreateView):
    model = Page
    template_name = "create_page.html"
    fields = "__all__"
    success_url = "/praca_/all-pages-class/"


def post_view(request):
    context = {}
    context["all_posts"] = Post.objects.all()
    return render(request, "all_posts_func.html", context)


class PostCreateView(CreateView):
    model = Post
    template_name = "create_post.html"
    fields = "__all__"
    success_url = "/praca_/all-posts-class/"


class PostDetailView(DetailView):
    model = Post
    template_name = "detail-post-class.html"

class PageDetailView(DetailView):
    model = Page
    template_name = "detail-page-class.html"

class PageUpdateView(UpdateView):
    model = Page
    fields = ("title", "description")
    template_name = "update-page-class.html"
    success_url = "/praca_/all-pages-class/"



class PostUpdateView(UpdateView):
    model = Post
    fields = ("name", "content")
    template_name = "update-post-class.html"
    success_url = "/praca_/all-posts-class/"




class PageDeleteView(DeleteView):
    model = Page
    template_name = "delete-page.html"
    success_url = "/praca_/all-pages-class/"




class PostDeleteView(DeleteView):
    model = Post
    template_name = "delete-post.html"
    success_url = "/praca_/all-posts-class/"

class LiteratureListView(ListView):
    model = Literature
    template_name = "all_literature_class.html"

class LiteratureCreateView(CreateView):
    model = Literature
    template_name = "create_literature.html"
    fields = "__all__"
    success_url = "/praca_/all_literature_class/"

class LiteratureDetailView(DetailView):
    model = Literature
    template_name = "detail_literature.html"


class LiteratureUpdateView(UpdateView):
    model = Literature
    fields = "__all__"
    template_name = "update-literature-class.html"
    success_url = "/praca_/all_literature_class/"


class LiteratureDeleteView(DeleteView):
    model = Literature
    template_name = "delete_literature.html"
    success_url = "/praca_/all_literature_class/"





