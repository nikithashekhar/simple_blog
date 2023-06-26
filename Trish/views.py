from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, EditComment
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

def LikeView(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id = post.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article_view', args = [str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    # ordering = ['-id']
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

# def index(request):
#     object_list = Post.objects.all()
#     return render(request, 'home.html', {'object_list' : object_list})

def AddCatListView(request):
    category_lists = Category.objects.all()
    return render(request, 'cat_list.html', {'category_lists' : category_lists})

def AddCatView(request, cat):
    category_posts = Post.objects.filter(category__iexact = cat)
    return render(request, 'cat.html', {'cat' : cat.title(), 'category_posts' : category_posts})

class DeetView(DetailView):
    model = Post
    template_name = 'deet.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DeetView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id = self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id = self.request.user.id).exists():
            liked = True
        context['cat_menu'] = cat_menu
        context['total_likes'] = total_likes
        context['liked'] = liked 
        return context

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    fields = '__all__'

class AddComment(CreateView):
    model = Comment
    form_class = EditComment
    template_name = 'add_comment.html'
    # fields = '__all__'
    ordering = ['-comment_date']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

class AddCat(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_cat.html'
    fields = '__all__'

class EditPost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_Post.html'
    # fields = {'title', 'title_tag', 'body'}

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

