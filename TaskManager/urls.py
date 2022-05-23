"""TaskManager URL Configuration

"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from TaskManager import settings, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name="dashboard"),
    path('task/create', views.create_task, name="create_task"),
    path('tasks', views.all_tasks, name="all_tasks"),
    path('task/completed/<int:task_id>', views.mark_completed, name="mark_completed"),
    path('task/delete/<int:task_id>', views.delete_task, name="delete_task"),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)