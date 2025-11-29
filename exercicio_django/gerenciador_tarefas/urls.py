from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    path('register/', core_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('task/<int:task_id>/complete/', core_views.complete_task, name='complete_task'),
    path('task/<int:task_id>/delete/', core_views.delete_task, name='delete_task'),
]