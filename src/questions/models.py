from django.db import models
from django.conf import settings


class Question(models.Model):
    """A coding question created by a user (author)."""

    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Link to the author (user who created the question)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="questions"
    )

    def __str__(self):
        return self.title


class TestCase(models.Model):
    """A test case belonging to a coding question."""

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="test_cases"
    )
    input_data = models.TextField(help_text="The input that will be passed to the program")
    expected_output = models.TextField(help_text="The expected output for the given input")

    def __str__(self):
        return f"TestCase for {self.question.title}"
