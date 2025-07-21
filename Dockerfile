# pull official base image
FROM python:3.12-slim-bookworm

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 

WORKDIR /app

RUN apt-get update && apt-get install -y curl
# install uv
COPY --from=ghcr.io/astral-sh/uv:0.6.17 /uv /uvx /bin/

COPY src/requirements.txt .
RUN uv pip install -r requirements.txt --system

COPY src/ .
# # Since there's no point in shipping lock files, we move them
# # into a directory that is NOT copied into the runtime image.
# # The trailing slash makes COPY create `/_lock/` automagically.
# COPY pyproject.toml uv.lock /_lock/

# # Synchronize dependencies.
# # This layer is cached until uv.lock or pyproject.toml change.
# RUN --mount=type=cache,target=/root/.cache \
#     cd /_lock && \
#     uv sync \
#     --frozen \
#     --no-install-project

# # copy project
# COPY . .

#EXPOSE to port 8000
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# Use gunicorn on port 8000
# CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "django_project.wsgi"]