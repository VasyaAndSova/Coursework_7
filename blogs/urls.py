from django.urls import path

from blogs.apps import BlogsConfig
from blogs.views import BlogListView, BlogDetail, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = BlogsConfig.name

urlpatterns = [
    path("blog/list/", BlogListView.as_view(), name="blog_list"),
    path("blog/detail/<int:pk>/", BlogDetail.as_view(), name="blog_detail"),
    path("blog/create/", BlogCreateView.as_view(), name="blog_create"),
    path("blog/update/<int:pk>/", BlogUpdateView.as_view(), name="blog_update"),
    path("blog/delete/<int:pk>/", BlogDeleteView.as_view(), name="blog_delete")

]