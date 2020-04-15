from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag
from django.views.generic import View
from django.urls import reverse
from .utils import *
from .forms import *
from django.core.paginator import Paginator
from django.db.models import Q

def posts_list(request):
################ For searching ########################
    search_query = request.GET.get('search', '')

    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Post.objects.all()
##############################################
    paginator = Paginator(posts,5)

    page_num = request.GET.get('page',1)
    page = paginator.get_page(page_num)

    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''
    context = {
        'posts': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }

    # return render(request, 'blog/index.html', context={'posts': posts})
    return render(request, 'blog/index.html', context=context)

class PostDetail(ObjectDetailMixin,View):
    model = Post
    template = 'blog/post_detail.html'
class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'blog/post_create_form.html'

class PostUpdate(ObjectUpdateMixit, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'
class PostDelete(ObjDeleteMixin,View):
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'post_list_url'


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})

class TagUpdate(ObjectUpdateMixit,View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'


class TagCreate(ObjectCreateMixin,View):
    model_form = TagForm
    template = 'blog/tag_create.html'
class TagDelete(ObjDeleteMixin,View):
    model = Tag
    template = 'blog/tag_delete_form.html'
    redirect_url = 'tags_list_url'

class TagDetail(ObjectDetailMixin,View):
    model = Tag
    template = 'blog/tag_detail.html'
def advertisement(request):
    n = "my thinks"
    return render(request, 'blog/advertisement.html', context={'post': n})


