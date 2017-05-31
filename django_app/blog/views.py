from django.shortcuts import render,HttpResponse

from blog.models import Post


def main_view(request):
    post = Post.objects.all()
    context = {
        'posts': post
    }
    return render(request, 'base/base.html', context)

