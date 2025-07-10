from django.urls import path
from . import views

urlpatterns = [
    path("",views.StartingPageView.as_view(), name="starting-page"),  # Define the starting page URL with the name "starting_page"),
    path("posts", views.AllPostsView.as_view(), name="posts-page"),  # Define the posts URL with the name "posts"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post-detail-page"),  # Define the post detail URL with the name "post_detail" and a slug parameter.
]