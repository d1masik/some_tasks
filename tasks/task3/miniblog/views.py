from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, PostComment
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import CommentsForm


# Create your views here.
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post/post_list.html'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post/post_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        comments = PostComment.objects.all()
        data['comments'] = comments
        if self.request.user.is_authenticated:
            data['comment_form'] = CommentsForm(instance=self.request.user)
        return data

    def post(self, request, *args, **kwargs):
        new_comment = PostComment(body=request.POST.get('body'),
                                  user=self.request.user,
                                  post=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)


class PostCreateView(CreateView):
    model = Post
    fields = ['theme', 'description', 'data', 'photo']
    success_url = reverse_lazy('posts')
    template_name = 'post/post_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    fields = ['theme', 'description', 'data', 'photo']
    success_url = reverse_lazy('posts')
    template_name = 'post/post_create.html'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/post_confirm_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('posts')




class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    fields = ['theme', 'description', 'data', 'photo']
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    # template_name = 'auth/logout.html'
    next_page = '/'


class CustomRegisterView(FormView):
    template_name = 'auth/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(CustomRegisterView, self).form_valid(form)




