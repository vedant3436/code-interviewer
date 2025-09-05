from django.urls import path

from .views import QuestionCreateView, QuestionDeleteView, QuestionDetailView, QuestionListView, QuestionUpdateView, TestCaseCreateView, TestCaseDeleteView

app_name = "questions"

urlpatterns = [
    path("", QuestionListView.as_view(), name="question-list"),
    path("<int:pk>/", QuestionDetailView.as_view(), name="question-detail"),
    path("create/", QuestionCreateView.as_view(), name="question-create"),
    path("<int:pk>/delete/", QuestionDeleteView.as_view(), name="question-delete"),
    path("<int:pk>/update/", QuestionUpdateView.as_view(), name="question-update"),

    #testcase
    path("<int:pk>/testcases/add/", TestCaseCreateView.as_view(), name="testcase-add"),
    path("testcases/<int:pk>/delete/", TestCaseDeleteView.as_view(), name="testcase-delete"),
]
