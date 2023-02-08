from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



from .models import Post
from .forms import CommentForm
from taggit.models import Tag

# Create your views here.


def post_list(request, tag_slug=None):
    post_list = Post.published.all()

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])

    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try: 
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render (request, 'list.html', {
        'posts': posts,
        'tag': tag,

    })


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

