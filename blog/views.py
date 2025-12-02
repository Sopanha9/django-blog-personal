from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag

# Homepage + Post list
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(is_published=True).order_by('-published_at')

# Single post page (with comments later)
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'