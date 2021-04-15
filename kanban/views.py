...
from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse_lazy # 追加
from django.views.generic import DetailView, UpdateView, CreateView,ListView # 追加

from .forms import UserForm, ListForm # 追加
from . models import List # 追加
...

...
class ListCreateView(LoginRequiredMixin, CreateView):
    model = List
    template_name = "kanban/lists/create.html"
    form_class = ListForm
    success_url = reverse_lazy("kanban:home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
