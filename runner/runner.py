import subprocess
import sys

def run_user_code(code_file_path):
    try:
        result = subprocess.run(
            ['python3', code_file_path],
            capture_output=True,
            text=True,
            timeout=5  # Optional: prevent infinite loops
        )
        return {
            "output": result.stdout,
            "errors": result.stderr,
            "exit_code": result.returncode
        }
    except subprocess.TimeoutExpired:
        return {
            "output": "",
            "errors": "Execution timed out.",
            "exit_code": -1
        }

if __name__ == "__main__":
    code_path = sys.argv[1]  # Get code file path from command line
    result = run_user_code(code_path)
    
    print("===OUTPUT===")
    print(result["output"])
    print("===ERRORS===")
    print(result["errors"])
    print("===EXIT_CODE===")
    print(result["exit_code"])

    print("sys argv:", sys.argv)
