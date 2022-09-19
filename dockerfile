# Build a "BaseImage" This is the first software our Docker has
FROM python:3.10

# Set environment variables

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory (OPT is UIX Optional Folder where we  download and run allexternal or 3rd party applications, similar to program files on windows)

RUN mkdir -p /opt/services/syntaxboard_django_3/src

WORKDIR /opt/services/syntaxboard_django_3/src

# Copy the Python Library Names and versions of required foor our Application
#
COPY ./requirements.txt .

# install the specified libraries
#
RUN pip install --no-cache-dir -r requirements.txt

# The Project code is copied from the folder where this Dockerfile is located
#
COPY . /opt/services/syntaxboard_django_3/src



# This Command Binds Django Appliation to Gunicorn Web Server
# 
CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD ["gunicorn", "--bind", ":8001", "--workers", "1", "syntaxboard_django_3.wsgi:application"]

EXPOSE 8001