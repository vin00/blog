from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.blog_list, name="blog_list"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("create/", views.blog_create, name="blog_create"),
    path("<int:pk>/update/", views.blog_update, name="blog_update"),
    path("<int:pk>/delete/", views.blog_delete, name="blog_delete"),
    path("tag/<str:tag>/", views.blog_tag, name="blog_tag"),
    path(
        "comment/<int:pk>/delete/",
        views.blog_comment_delete,
        name="blog_comment_delete",
    ),
]
