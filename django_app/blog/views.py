from django.shortcuts import render, HttpResponse, redirect

from blog.forms import PostCreationForm
from blog.models import Post
from django.contrib.auth import get_user_model

User = get_user_model()

def main_view(request):
    post = Post.objects.all()
    context = {
        'posts': post
    }
    return render(request, 'post/post-list.html', context)

def post_add_view(request):
    if request.method == 'GET':
        form = PostCreationForm()

        context = {
            'forms': form
        }

        return render(request, 'post/post-add.html', context)

    elif request.method == 'POST':
        form = PostCreationForm(request.POST)

        if form.is_valid():
            author = User.objects.first()
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            Post.objects.create(
                author=author,
                title=title,
                text=text,
            )
        return redirect('post_main')