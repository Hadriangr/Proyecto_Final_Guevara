# blog/views.py
from django.shortcuts import render, redirect
from django.views import View
from django.utils import timezone  # Importa la función timezone
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


class Crearblogview(View):
    template_name = 'crear_blog.html'

    def get(self, request):
        form = PostForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()  # Establece la fecha de publicación
            post.save()
            return redirect('post_list')

        return render(request, self.template_name, {'form': form})