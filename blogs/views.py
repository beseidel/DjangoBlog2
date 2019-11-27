



#queryset based
#
# from django.shortcuts import render
# from .models import Post
#
#
# def index(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'index.html', context)
#
#
# def about(request):
#     return render(request, 'about.html', {'title': 'About'})
#

#
# *****************************************************

from django.shortcuts import render
from .models import Post

# Create your views here.

from django.http import HttpResponse

# function based
# def index(request):
#     return HttpResponse ('<h1>blogs home<h1>')
#
# def about(request):
#     return HttpResponse ('<h1>blogs about<h1>')


# ******************************************
#
# posts = [
#      {
#
#       'author': 'Barbara Seidel',
#       'title': 'Blog Post 1',
#       'content': 'first post content',
#       'date_posted': 'August 27, 2019',
#
#       },
#
#       {
#
#       'author': 'Barbara Seidel',
#       'title': 'Blog Post 2',
#       'content': 'Second post content',
#       'date_posted': 'August 28, 2019',
#
#       }
#  ]
# # # template based
# def home(request):
#      context = {
#           'posts': posts
#        }
#
#      return render (request, 'home.html', context)
#
# def index(request):
#      context = {
#           'posts': posts
#       }
#
#      return render (request, 'index.html', context)
#
# def about(request):
#      return render (request, 'about.html', {'title': 'About' } )
#
#
#
# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('blogs-home')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'register.html', {'form': form})
#
#
# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('blogs-home'))
#         form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user and bcrypt.check_password_hash(user.password, form.password.data):
#             login_user(user, remember=form.remember.data)
#             next_page = request.args.get('next')
#             return redirect(next_page) if next_page else redirect(url_for('blogs-home'))
#         else:
#             flash('Login Unsuccessful. Please check email and password', 'danger')
#     return render_template('login.html', title='Login', form=form)
#
#
# #
# @app.route("/logout")
# def logout():
#     logout_user()
#     return redirect(url_for('blogs-home'))
#
#
# @app.route("/account")
# @login_required
# def account():
#     return render_template('account.html', title='Account')

#
# ************
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'about.html', {'title': 'About'})


# queryset based
#
# from django.shortcuts import render
# from .models import Post
#
#
# def index(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'index.html', context)
#
#
# def about(request):
#     return render(request, 'about.html', {'title': 'About'})
#

#
# *****************************************************

# from django.shortcuts import render
# from .models import Post

# Create your views here.

from django.http import HttpResponse

# function based
# def index(request):
#     return HttpResponse ('<h1>blogs home<h1>')
#
# def about(request):
#     return HttpResponse ('<h1>blogs about<h1>')


#
# posts = [
#      {
#
#       'author': 'Barbara Seidel',
#       'title': 'Blog Post 1',
#       'content': 'first post content',
#       'date_posted': 'August 27, 2019',
#
#       },
#
#       {
#
#       'author': 'Barbara Seidel',
#       'title': 'Blog Post 2',
#       'content': 'Second post content',
#       'date_posted': 'August 28, 2019',
#
#       }
#  ]
# # # template based
# def home(request):
#      context = {
#           'posts': posts
#        }
#
#      return render (request, 'home.html', context)
#
# def index(request):
#      context = {
#           'posts': posts
#       }
#
#      return render (request, 'index.html', context)
#
# def about(request):
#      return render (request, 'about.html', {'title': 'About' } )
