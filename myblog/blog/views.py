from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post
from .form import CommentsForm


class PostView(View):
    """Вывод записей"""

    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/blog.html', {'post_list': posts})


class PostDerail(View):
    """Отдельная страница по записям"""

    def get(self, request, pk):
        posts = Post.objects.get(id=pk)
        return render(request, 'blog/blog_detail.html', {'post': posts})


class AddComments(View):
    """Добавление комментариев"""

    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')
