from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
def index(request):
    return render(request, "kanban/index.html") # このように変更する

