from django.urls import path
from . import views

from django.shortcuts import redirect

def home_redirect(request):
    return redirect('login')

urlpatterns = [
    path('', home_redirect, name='home'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('project/new/', views.ProjectCreateView.as_view(), name='project_create'),
    path('project/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('project/<int:pk>/edit/', views.ProjectUpdateView.as_view(), name='project_edit'),
    path('project/<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project_delete'),
    path('profile/', views.ProfileUpdateView.as_view(), name='profile'),
    path('project/<int:project_pk>/task/new/', views.TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task_edit'),
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
    path('category/new/', views.CategoryCreateView.as_view(), name='category_create'),

]