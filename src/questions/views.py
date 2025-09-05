from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Question, TestCase

class QuestionListView(ListView):
    model = Question
    template_name = "questions/questions_list.html"
    context_object_name = "questions"

class QuestionDetailView(DetailView):
    model = Question
    template_name = "questions/question_detail.html"
    context_object_name = "question"

class QuestionCreateView(CreateView):
    model = Question
    fields = ["title", "description"]
    template_name = "questions/question_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class QuestionUpdateView(UpdateView):
    model = Question
    fields = ["title", "description"]
    template_name = "questions/question_form.html"

class QuestionDeleteView(DeleteView):
    model = Question
    template_name = "questions/question_confirm_delete.html"
    success_url = reverse_lazy("questions:question-list")

class TestCaseCreateView(CreateView):
    model = TestCase
    fields = ["input_data", "expected_output"]
    template_name = "questions/testcase_form.html"

    def form_valid(self, form):
        question = get_object_or_404(Question, pk=self.kwargs["pk"])
        form.instance.question = question
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("question:question-detail", kwargs={"pk": self.kwargs["pk"]})
    
class TestCaseDeleteView(DeleteView):
    model = TestCase
    template_name = "questions/testcase_confirm_delete.html"

    def get_success_url(self):
        return reverse("questions:question-detail", kwargs={"pk": self.objectve.question.pk})


