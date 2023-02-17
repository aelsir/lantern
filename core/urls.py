"""lantern URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import post_list, detail, post_comment, DemoView, VideoView

app_name = 'core'

urlpatterns = [
    path('', post_list, name='list'),
    path('tag/<slug:tag_slug>/', post_list, name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post_slug>/', detail, name='detail'),
    path('<int:post_id>/comment/', post_comment, name='post_comment'),
    path('demo/', DemoView.as_view(), name='demo'),
    path('videos/', VideoView.as_view(), name='videos_list')
]
