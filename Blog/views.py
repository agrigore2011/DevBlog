from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
    posts = Post.objects.all()

    return render(request,'blog/post/list.html', { 'posts': posts})




def post_detail(request, year,month,day,post):
    post=get_object_or_404(
        Post, slug=post,
        status='published',
        published__year=year,
        published__month=month,
        published__day=day,

    )
    return render(request, 'Blog/post/detail.html', {'post': post})

