from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from blog.models import Post
from blog.services import send_post_email


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(published=True)
        return queryset


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        """Функция для получения контекта c целью увеличения кол-ва просмотров"""
        context_data = super().get_context_data(**kwargs)
        context_data['name'] = self.get_object()
        obj = self.get_object()
        increase = get_object_or_404(Post, pk=obj.pk)
        increase.increase_views() # увеличение количества просмотров
        if increase.increase_views == 50:
            send_post_email(increase)  # отправка письма
        return context_data



class PostCreateView(CreateView):
    model = Post

    fields = ('name', 'content', 'image', 'published')
    success_url = reverse_lazy('blog:post_list')


class PostUpdateView(UpdateView):
    model = Post
    fields = ('name', 'content', 'image', 'published')
    success_url = reverse_lazy('blog:post_list')


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')


class PostUpdateView(UpdateView):
    model = Post
    fields = ('name', 'content', 'image', 'published')

    def get_success_url(self):
        return reverse('blog:post_item', args=[str(self.object.pk)])


def toggle_publish(pk):
    post_item = get_object_or_404(Post, pk=pk)
    if post_item.published:
        post_item.published = False
    else:
        post_item.published = True

    post_item.save()

    return redirect(reverse('blog:blog_item', args=[post_item.pk]))
