from django.urls import path

from .views import PlaygroundPageView, run_code

urlpatterns = [
    path("", PlaygroundPageView.as_view(), name="playground"),
    path("run_code/", run_code, name="run_code"),
]
