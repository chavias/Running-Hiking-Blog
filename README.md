# Flask Blog

This is a simple blog application built with Flask, a lightweight web framework for Python. The application is containerized using Docker to ensure consistency across different environments.

## Features

- Create, read, update, and delete blog posts
- User authentication and authorization
- Responsive design using Bootstrap
- 

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Docker installed on your machine
- Docker Compose (optional, but recommended for multi-container applications)
- Python 3.x installed (for local development)

## Getting Started

Follow these instructions to set up and run the application.

### Clone the Repository

```bash
git clone https://github.com/your-username/flask-blog.git
cd flask-blog
```

## Build and Run the Docker Container

1. Create a .env file. You can use the provided .env.example file as a   template to create your .env file:
    ```bash
    cp .env.example .env
    vim .env # or emacs, nano, etc.
    ```

2. Build the Docker image:

    ```bash
    docker build -t flask_blog .
    ```

3. Run the Docker container:

    ```bash
    docker run -p 5000:5000 flask_blog
    ```

### Using Docker Compose

For easier management you can use Docker Compose. You can use the provided docker-compose.yml file or adapt it to your needs.

1. As before create a .env file. You can use the provided .env.example file as a   template to create your .env file:
   
    ```bash
    cp .env.example .env
    vim .env # or emacs, nano, etc.
    ```

2. Edit docker-compose.yml
   
   ```bash
   vim docker-compose.yml
   ```

3. Build and run the containers:

    ```bash
    docker-compose up --build
    ```

## Accessing the Application

Once the container is running, you can access the application at http://localhost:5000.

## Application Structure

```
.
├── docker-compose.debug.yml
├── docker-compose.yml
├── Dockerfile
├── flaskblog
│   ├── config.py
│   ├── errors
│   │   ├── handlers.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── main
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── models.py
│   ├── posts
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── static
│   │   ├── main.css
│   │   └── profile_pics
│   ├── templates
│   │   ├── about.html
│   │   ├── account.html
│   │   ├── create_post.html
│   │   ├── errors
│   │   │   ├── 403.html
│   │   │   ├── 404.html
│   │   │   └── 500.html
│   │   ├── home.html
│   │   ├── layout.html
│   │   ├── login.html
│   │   ├── post.html
│   │   ├── register.html
│   │   ├── reset_request.html
│   │   ├── reset_token.html
│   │   └── user_posts.html
│   └── users
│       ├── forms.py
│       ├── __init__.py
│       ├── routes.py
│       └── utils.py
├── instance
│   └── site.db
├── README.md
├── requirements.txt
└── run.py
```

## License

This project is licensed under the MIT License. For further details, refer to the [LICENSE](LICENSE) file.
