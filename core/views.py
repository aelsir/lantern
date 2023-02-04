from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.http import HttpResponseRedirect



from .models import Post, Comment
from .forms import CommentForm

# Create your views here.


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'list.html'


def detail(request, year, month, day, post_slug):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post_slug, publish__year=year, publish__month=month, publish__day=day)

    # get all of the post comments
    comments = post.comments.filter(active=True)
    form = CommentForm()

    return render(request, 'detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })

# Saving the comment into the database
@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return HttpResponseRedirect(post.get_absolute_url())

