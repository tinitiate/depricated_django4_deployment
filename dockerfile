# Build a "BaseImage" This is the first software our Docker has
FROM python:3.10

# Set environment variables

# The "PIP_DISABLE_PIP_VERSION_CHECK" environment variable is used to control whether pip, the package installer for Python, checks for updates to itself. 
# If you set this variable to "1"it disables the version check, meaning pip will not check for updates to its own version. 
ENV PIP_DISABLE_PIP_VERSION_CHECK 1

# The "PYTHONDONTWRITEBYTECODE" environment variable is used to control whether Python writes bytecode files to disk or not. When set to "1," it prevents Python from generating ".pyc" (bytecode) files. 
# Bytecode files are intermediate files created by Python to improve the loading time of Python scripts, but they are not essential for running Python code.
ENV PYTHONDONTWRITEBYTECODE 1

# The "PYTHONUNBUFFERED" environment variable is used to control the buffering behavior for standard input and output streams in Python. 
# When set to "1," it disables the buffering of these streams, making the output immediately visible in the terminal or log files as soon as it's produced, without waiting for a buffer to fill up.
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
