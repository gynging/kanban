from django.urls import path

from . import views

app_name = "kanban"

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.HomeView.as_view(), name="home"),
    path("signup/", views.signup, name="signup"),
    path("users/<int:pk>/", views.UserDetailView.as_view(), name="users_detail"), # 追加
]
