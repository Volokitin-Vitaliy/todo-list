from django.urls import path
from .views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskToggleDoneView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

app_name = "task"

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("task/add/", TaskCreateView.as_view(), name="task_add"),
    path("task/<int:pk>/edit/", TaskUpdateView.as_view(), name="task_edit"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
    path("task/<int:pk>/toggle/", TaskToggleDoneView.as_view(), name="task_toggle"),
    path("tag/add/", TagCreateView.as_view(), name="tag_add"),
    path("tag/<int:pk>/edit/", TagUpdateView.as_view(), name="tag_edit"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag_delete"),
]
