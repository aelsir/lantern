# import libraries and functions
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.decorators.http import require_POST
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from taggit.models import Tag
from .forms import CommentForm
# import from local files
from .models import EmailSubscription, Post, Video

# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = 'list.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        tag_slug = self.kwargs.get('tag_slug')
        query = self.kwargs.get('title')
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            return Post.published.filter(tags=tag)
        if query:
            return Post.published.filter(title__icontains=query)
        else:
            return Post.published.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.kwargs.get('tag_slug')
        return context


postList = PostListView.as_view()


class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'post_slug'
    queryset = Post.objects.filter(
        status=Post.Status.PUBLISHED,
        publish__lte=timezone.now()
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()

        context['similar_posts'] = post.tags.similar_objects()[:3]
        context['comments'] = post.comments.filter(active=True)
        context['form'] = CommentForm()

        return context

detail = PostDetailView.as_view()

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

class SubscribeView(View):
    template_name = 'partial/subscribe.html'
    success_url = reverse_lazy('core:list')

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        EmailSubscription.objects.create(email=email)
        messages.success(request, 'Subscribed!')
        return redirect(self.success_url)

subscribe = SubscribeView.as_view()

class VideoView(ListView):
    model = Video
    template_name = 'videos_list.html'
    context_object_name = 'videos'


# just a demo and trial view
class DemoView(TemplateView):
    template_name = 'demo.html'
