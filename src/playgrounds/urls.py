from django.urls import path

from .views import PlaygroundPageView, run_code_view, get_task_result_view

urlpatterns = [
    path("", PlaygroundPageView.as_view(), name="playground"),
    #path("run_code/", run_code, name="run_code"),
    path("run_code/", run_code_view, name="run_code"),
    path("get_result/", get_task_result_view, name="get_result"),
]
