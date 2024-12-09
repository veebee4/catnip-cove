from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
    path("add/", views.add_blog, name="add_blog"),
    path("edit/<int:post_id>/", views.edit_blog, name="edit_blog"),
    path("delete/blog-post/<int:post_id>/", views.delete_blog, name="delete_blog"),
    path("delete/comment/<int:comment_id>/", views.delete_comment, name="delete_comment"),
]