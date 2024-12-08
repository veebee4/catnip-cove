from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
    path("add/", views.add_blog, name="add_blog"),
    path("edit/<int:post_id>/", views.edit_blog, name="edit_blog"),
]