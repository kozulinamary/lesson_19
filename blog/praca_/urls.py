from django.urls import path, include
from .views import hello, page_view, PageListView, PageCreateView, post_view, Page_ListView, PostCreateView, PostDetailView, PageDetailView,PageUpdateView,PostUpdateView, PageDeleteView, PostDeleteView, LiteratureListView, LiteratureCreateView, LiteratureDetailView, LiteratureUpdateView, LiteratureDeleteView



urlpatterns = [
    path("hello/", hello, name="hello"),
    path("all-pages-func/", page_view, name="all_pages_func"),
    path("all-pages-class/", PageListView.as_view(), name="all_pages_class"),
    path('create_page/', PageCreateView.as_view(), name="create_page"),
    path("all-posts-func/", post_view, name="all_posts_func"),
    path("all-posts-class/", Page_ListView.as_view(), name="all_posts_class"),

    path('create_post/', PostCreateView.as_view(), name="create_post"),
    path('detail_post/<int:pk>', PostDetailView.as_view(), name="detail_post"),
    path('detail_page/<int:pk>', PageDetailView.as_view(), name="detail_page"),
    path('update_page/<int:pk>', PageUpdateView.as_view(), name="update_page"),
    path('update_post/<int:pk>', PostUpdateView.as_view(), name="update_post"),
    path('delete_page/<int:pk>', PageDeleteView.as_view(), name="delete_page"),
    path('delete_post/<int:pk>', PostDeleteView.as_view(), name="delete_post"),
    path("all_literature_class/", LiteratureListView.as_view(), name="all_literature_class"),
    path('create_literature/', LiteratureCreateView.as_view(), name="create_literature"),
    path('detail_literature/<int:pk>', LiteratureDetailView.as_view(), name="detail_literature"),
    path('update-literature/<int:pk>', LiteratureUpdateView.as_view(), name="update-literature"),
    path('delete_literature/<int:pk>', LiteratureDeleteView.as_view(), name="delete_literature"),



]