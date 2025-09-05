from django.contrib import admin
from .models import Question, TestCase

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    search_fields = ("title", "description", "author__username")

@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ("question", "input_data", "expected_output")
