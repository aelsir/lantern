# import libraries and functions
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.db.models import Count
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from taggit.models import Tag


# import from local files
from .models import Post, Video
from .forms import CommentForm

# Create your views here.

# the main function which display the list of the posts written in the blog.
def post_list(request, tag_slug=None):
    post_list = Post.published.all()

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])

    paginator = Paginator(post_list, 6)
    page_number = request.GET.get('page', 1)
    try: 
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    # I should change this to list.html after finising
    return render (request, 'demo.html', {
        'posts': posts,
        'tag': tag,

    })

# displaying a details for a single choosen blog with it's comments
def detail(request, year, month, day, post_slug):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, 
                             slug=post_slug, 
                             publish__year=year, 
                             publish__month=month, 
                             publish__day=day)

    # get all of the active post comments
    comments = post.comments.filter(active=True)
    form = CommentForm()

    # get the list of similar post
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', 'publish')[:3]
    
    return render(request, 'detail.html', {
        'post': post,
        'similar_posts': similar_posts,
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


class VideoView(ListView):
    model = Video
    template_name = 'videos_list.html'
    context_object_name = 'videos'

# just a demo and trial view
class DemoView(TemplateView):
    template_name = 'demo.html'

