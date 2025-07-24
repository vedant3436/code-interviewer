from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt # This disables CSRF protection for a specific view
import json
import os
from uuid import uuid4
import subprocess

class PlaygroundPageView(TemplateView):
    template_name = "playgrounds/playground.html"

@csrf_exempt #temporary post without csrf token 
def run_code(request):
    # if request.method == "POST":
    #     data = json.loads(request.body)

    #     code = data.get("code", "")

    #     return JsonResponse({
    #         "stdout": code,
    #         "stderr": "",
    #         "exit_code": 0
    #     })
    
    # return JsonResponse({"error": "Post required"}, status=405)

    if request.method != "POST":
        return JsonResponse({"error": "Only POST method allowed"}, status=405)
    
    try:
        data = json.loads(request.body)
        code = data.get("code")
    except:
        return JsonResponse({"error": "Invalid JSON"}, status = 400)
        
    if not code:
        return JsonResponse({"error": "No code provided"}, status = 400)
    
    #create unique filename
    filename = f"{uuid4().hex}.py" 
    temp_dir = os.path.join("temp")
    os.makedirs(temp_dir, exist_ok = True)
    file_path = os.path.join(temp_dir, filename)

    #write code to file
    with open(file_path, "w") as f:
        f.write(code)

    try:
        #run the code in the runner container
        command = [
            "docker", "compose", "run", "--rm",
            "runner", f"temp/{filename}"
        ]
        
        result = subprocess.run(command, capture_output=True, text=True, timeout=10)

        output = result.stdout
        errors = result.stderr
        exit_code = result.returncode

    except subprocess.TimeoutExpired:
        output = ""
        errors = "Execution time out."
        exit_code = -1

    finally:
        #cleanup (optional)
        try:
            os.remove(file_path)
        except OSError:
            pass

    print(f"output = {output}")
    print(f"errors = {errors}")
    print(f"exit code = {exit_code}")
    print(f"code = {code}")

    return JsonResponse({
        "output": output,
        "errors": errors,
        "exit_code": exit_code
    })

