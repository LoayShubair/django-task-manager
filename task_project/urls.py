"""
URL configuration for task_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from tasks.views import (
    task_list,
    task_detail,
    task_create,
    task_edit,
    task_delete,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", task_list, name="task_list"),
    path("task/<int:pk>/", task_detail, name="task_detail"),
    path("task/create/", task_create, name="task_create"),
    path("task/<int:pk>/edit/", task_edit, name="task_edit"),
    path("task/<int:pk>/delete/", task_delete, name="task_delete"),
]
