# Dockerfile

## Base Image

- In Docker, a **"base image"** refers to the starting point or the foundation on which we build your Docker containers. 
- It serves as the core of the container and contains a minimal operating system with pre-installed packages, libraries, and tools that are necessary to run specific types of applications. 
- Base images can be official images provided by Docker Hub or custom images created by users or organizations.
- When we create a new container, Docker pulls the base image specified in your Dockerfile (using the `FROM` instruction) from a container registry (such as Docker Hub) and uses it as the base to add our application code and additional dependencies. 
- This layered approach allows Docker to reuse common components across multiple containers, making the containers lightweight and easy to distribute.

- We use the Python 3.10 image as the base image for our Docker container 

  ``` dockerfile
  FROM Python 3.10-bullseye
  ```

## Environment Variables in Docker

- In Docker, **environment variables** are variables that can be set within a container to configure its runtime behavior and customize the application environment. 
- These variables are accessible by processes running inside the container, allowing you to pass configuration parameters, credentials, or other dynamic values to your applications without modifying the application code or configuration files.

### Setting Environment Variables in Dockerfile

- We can define environment variables directly in the Dockerfile using the `ENV` instruction. 

  ```dockerfile
  ENV PIP_DISABLE_PIP_VERSION_CHECK 1
  ENV PYTHONDONTWRITEBYTECODE 1
  ENV PYTHONUNBUFFERED 1
  ```

### Explanation of Specific Environment Variables:

#### 1. `ENV PIP_DISABLE_PIP_VERSION_CHECK 1`

- The environment variable `PIP_DISABLE_PIP_VERSION_CHECK` is used to control whether pip, the package installer for Python, checks for updates to itself.
- When set to `1`, it disables the version check, meaning pip will not check for updates to its own version. 
- It is common to disable the pip version check in containerized environments where you typically manage the package versions explicitly.

#### 2. `ENV PYTHONUNBUFFERED 1`

- The environment variable `PYTHONUNBUFFERED` is used to control the buffering behavior for standard input and output streams in Python. 
- When set to `1`, it disables the buffering of these streams, making the output immediately visible in the terminal or log files as soon as it's produced, without waiting for a buffer to fill up.
- This is particularly useful in Docker containers because it allows you to see the application's logs in real-time, making debugging and troubleshooting easier.

#### 3. `ENV PYTHONDONTWRITEBYTECODE 1`

- The environment variable `PYTHONDONTWRITEBYTECODE` is used to control whether Python writes bytecode files to disk or not. 
- When set to `1`, it prevents Python from generating `.pyc` (bytecode) files. Bytecode files are intermediate files created by Python to improve the loading time of Python scripts, but they are not essential for running Python code.
- In containerized environments, it is common to disable bytecode generation to reduce unnecessary file writes and disk usage, especially in read-only filesystems used in some container configurations.

## Commands

- The `RUN` instruction is used in Dockerfile to execute the specified command during the image build process.

  ```dockerfile
  RUN mkdir -p /opt/services/syntaxboard_django_3/src
  ```

  - This command creates a new directory path `/opt/services/syntaxboard_django_3/src` inside the Docker container. 

  -  The `-p` flag ensures that the parent directories are created if they don't already exist.

  ```dockerfile
  RUN pip install --no-cache-dir -r requirements.txt
  ```

  * This command installs Python packages listed in the `requirements.txt` file.
  * **`--no-cache-dir`:** This option tells `pip` not to use any cached files during the installation process. It ensures that the packages are downloaded and installed directly from the package index without relying on any previously cached data. Using this option can be beneficial to ensure you get the most up-to-date versions of the packages.

- The `WORKDIR` instruction is used to set the working directory for any `RUN`, `CMD`, `ENTRYPOINT`, `COPY`, and `ADD` commands that follow it. 

  ```dockerfile
  WORKDIR /opt/services/syntaxboard_django_3/src
  ```

  * In this case, it set the workingdirectory inside docker to  `/opt/services/syntaxboard_django_3/src`. 

- The `COPY` command copies files or directories from the host machine (where the Docker build is happening) to the container's file system. 

  ```dockerfile
  COPY ./requirements.txt .
  ```

  * In this case, it copies the file `requirements.txt` from the current directory (where the Dockerfile is located) on the host to the container's working directory, which is set to `/opt/services/syntaxboard_django_3/src` due to the previous `WORKDIR` instruction.

  ```dockerfile
  COPY . /opt/services/syntaxboard_django_3/src
  ```

  * This step copies the entire project code into the container, making it available for execution.

* The `CMD` instruction is used to specify the default command that should be executed when a container is run based on the image created from that Dockerfile. The `CMD` instruction defines the primary process that runs inside the container. If you define multiple `CMD` instructions in a Dockerfile, only the last one will take effect, and it will be used as the default command for the container.

* **Exec form:**

  ```dockerfile
  CMD ["executable", "param1", "param2", ...]
  ```

  * In the exec form, the command is specified as a JSON array of strings, where the first element is the executable, and subsequent elements are the parameters passed to the executable. The exec form is generally preferred for better compatibility and avoiding potential issues with shell-related problems.

  * ```CMD ["python", "manage.py", "makemigrations"]```

    This `CMD` instruction specifies the default command to be executed when a container is started from the Docker image.

    * `python`: This is the executable or binary for the Python interpreter. It tells Docker to use the Python interpreter to run the following command.
    * `manage.py`: This is the name of a Python script file. In Django projects, `manage.py` is a management script provided by Django that allows you to perform various administrative tasks related to the Django project.
    * `makemigrations`: This is a Django management command. The `makemigrations` command is used to create new database migration files based on changes to the Django models in the project. Database migrations are essential for keeping the database schema in sync with changes in the Django models, allowing you to apply these changes to the database in a version-controlled manner.

  * ``` CMD ["python", "manage.py", "migrate"]```

    * `python`: The executable or binary for the Python interpreter.
    * `manage.py`: The Django management script.
    * `migrate`: This is another Django management command. The `migrate` command is used to apply database migrations to the database, updating the schema based on the migration files generated by the `makemigrations` command.

  * ```CMD ["gunicorn", "--bind", ":8001", "--workers", "1", "syntaxboard_django_3.wsgi:application"]```

    * `gunicorn`: This is the executable or binary for Gunicorn, which stands for Green Unicorn, a popular WSGI server for Python web applications.
    * `--bind :8001`: This option tells Gunicorn to bind to port 8001. The application will be accessible through this port inside the container.
    * `--workers 1`: This option sets the number of worker processes Gunicorn will spawn to handle incoming requests. In this case, it's set to 1 worker process.
    * `syntaxboard_django_3.wsgi:application`: This is the entry point to the Django WSGI application that Gunicorn should serve. The WSGI application object is specified in the Django project's `wsgi.py` file.

