from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt # This disables CSRF protection for a specific view
import json

class PlaygroundPageView(TemplateView):
    template_name = "playgrounds/playground.html"

@csrf_exempt #temporary post without csrf token 
def run_code(request):
    if request.method == "POST":
        data = json.loads(request.body)

        code = data.get("code", "")

        return JsonResponse({
            "stdout": code,
            "stderr": "",
            "exit_code": 0
        })
    
    return JsonResponse({"error": "Post required"}, status=405)