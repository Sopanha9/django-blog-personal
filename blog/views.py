from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag, Comment
from django.shortcuts import redirect

# Homepage + Post list
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 6

    # def get_context_data(self, **kwargs):
    #     context =  super().get_context_data(**kwargs)
    #     context['test_message'] = "Welcome to the Blog!"
    #     return context



    def get_queryset(self):
        return Post.objects.filter(is_published=True).order_by('-published_at')

# Single post page (with comments later)
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_details.html'
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.filter(is_published=True)
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        name = request.POST.get('author_name')
        email = request.POST.get('author_email')
        content = request.POST.get('content')

        Comment.objects.create(
            post=self.object,
            author_name=name,
            author_email=email,
            content=content,
            approved=True  # moderation
        )
        return redirect(f"{self.object.get_absolute_url()}?commented=1")



