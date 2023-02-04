from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'list.html'


def detail(request, year, month, day, post_slug):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post_slug, publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'detail.html', {
        'post': post
    })
