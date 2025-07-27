from celery import shared_task
import subprocess
import uuid
import os

@shared_task
def run_code_task(code):
    filename = f"/app/temp/code_{uuid.uuid4().hex[:8]}.py"
    with open(filename, "w") as f:
        f.write(code)

    process = subprocess.run(
        ["python", filename],
        capture_output=True,
        text=True,
        timeout=5
    )
    os.remove(filename)
    return {
        "stdout": process.stdout,
        "stderr": process.stderr,
        "exit_code": process.returncode,
    }
