from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin # 追加
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, resolve_url
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy # 追加
from django.views.generic import DetailView, UpdateView, CreateView,ListView,DeleteView # 追加
from .forms import UserForm, ListForm # 追加
from .models import List,Card # 追加
from .forms import UserForm,CardForm
from .mixins import OnlyYouMixin

def index(request):
    return render(request, "kanban/index.html")
@login_required

def home(request):
    return render(request, "kanban/home.html")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_instance = form.save()
            login(request, user_instance)
            return redirect("kanban:home")
    else:
        form = UserCreationForm()
        context = {
            "form": form
        }
    return render(request, 'kanban/signup.html', context)

class ListCreateView(LoginRequiredMixin, CreateView):
    model = List
    template_name = "kanban/lists/create.html"
    form_class = ListForm
    success_url = reverse_lazy("kanban:lists_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UserDetailView(LoginRequiredMixin, DetailView): # この行を編集
    model = User
    template_name = "kanban/users/detail.html"

class UserUpdateView(OnlyYouMixin, UpdateView):
    model = User
    template_name = "kanban/users/update.html"
    form_class = UserForm

    def get_success_url(self):
        return resolve_url('kanban:users_detail', pk=self.kwargs['pk'])

class ListListView(LoginRequiredMixin, ListView):
    model = List
    template_name = "kanban/lists/list.html"

class ListDetailView(LoginRequiredMixin, DetailView):
    model = List
    template_name = "kanban/lists/detail.html"

class ListUpdateView(LoginRequiredMixin, UpdateView):
    model = List
    template_name = "kanban/lists/update.html"
    form_class = ListForm

    def get_success_url(self):
        return resolve_url('kanban:lists_detail', pk=self.kwargs['pk'])

class ListDeleteView(LoginRequiredMixin, DeleteView):
    model = List
    template_name = "kanban/lists/delete.html"
    success_url = reverse_lazy("kanban:lists_list")

class CardCreateView(LoginRequiredMixin, CreateView):
    model = Card
    template_name = "kanban/cards/create.html"
    form_class = CardForm
    success_url = reverse_lazy("kanban:home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)