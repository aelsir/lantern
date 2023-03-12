from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import EmailSubscription, Post

@shared_task
def send_blog_post_email(post_id):
    post = Post.objects.get(id=post_id)
    subscribers = EmailSubscription.objects.all()
    for subscriber in subscribers:
        subject = 'New blog post: {}'.format(post.title)
        message = 'Check out our new blog post at: {}'.format(post.get_absolute_url())
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [subscriber.email])
