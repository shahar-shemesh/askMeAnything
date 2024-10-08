# ASKMEANYTHING

## Overview

![askmeanything](https://github.com/user-attachments/assets/50227105-8382-468d-82fa-e972cfa31af9)


ASKMEANYTHING is a Flask-based application that allows users to ask questions, retrieves answers using the OpenAI API, and stores both questions and answers in a PostgreSQL database. The application is containerized using Docker and managed with Docker Compose. It also includes testing with pytest to ensure proper functionality.

## Directory Details

- **app/**: Contains the main application code.
  - **errors/**: Custom error handlers.
  - **main/**: Core application routes.
- **logs/**: Contains log files.
- **migrations/**: Alembic migration scripts.
- **tests/**: Contains pytest test files.
- **.env**: Environment variables.
- **.flaskenv**: Flask environment configuration.
- **alembic.ini**: Alembic configuration.
- **askMeAnything.py**: Entry point for the Flask application.
- **boot.sh**: Script to initialize the application.
- **config.py**: Configuration settings.
- **docker-compose.yml**: Docker Compose configuration.
- **Dockerfile**: Dockerfile for the Flask application.
- **requirements.txt**: Python dependencies.
- **utils.py**: Utility functions.

## Functionality

* Users can submit questions through a POST request to the `/ask` endpoint with a JSON payload containing the `question` field.
* The server leverages the OpenAI API to generate an answer for the provided question.
* Both the question and the generated answer are persisted in a PostgreSQL database for future reference.


## Requirements

1. **Flask Server**: Provides an endpoint to handle questions.
2. **OpenAI API Integration**: Fetches answers for questions.
3. **Database**: Uses PostgreSQL to store questions and answers.
4. **Alembic**: Manages database migrations.
5. **Docker**: Containerizes the Flask application and PostgreSQL database.
6. **Docker Compose**: Orchestrates and manages containers.
7. **Testing**: Validates endpoint functionality with pytest.


## Getting Started

To begin, ensure that Docker and Docker Compose are installed on your system.

If the PostgreSQL image already exists on your machine, it is advisable to rebuild it along with the application image to ensure compatibility.

 Next, follow these steps:

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/shahar-shemesh/askMeAnything.git
    ```

2. Navigate to the directory of the cloned repository:
    ```bash
    cd "askMeAnything"
    ```
    
3. Edit the `.env` file with your OpenAI API key:
    ```bash
    ...
    OPENAI_API_KEY=<your_openai_api_key>
    ...
    ```
    
4. Build and start containers:
    ```bash
    docker compose up --build
    ```

5. Access the Flask Application:
    - The Flask server will be available at `http://localhost:4000`
    - The database service will be available at `http://localhost:5432`



## Testing the Flask API

Once the services are up and running, you can test the app using various tools. Here’s how to use Postman and TablePlus to interact with flask server and database:

### Using Postman

Postman is a powerful API testing tool that allows you to send HTTP requests and view responses in a user-friendly interface. Follow these steps to test the API:

1.  Download Postman from the [official website](https://www.postman.com/downloads/) and install it on your machine.

2.  Send a POST request to `http://localhost:4000/ask` with a JSON payload (Body → ☑raw) containing the question field, for example:

```json
{
  "question": "What is the capital of France?"
}
```

### Using TablePlus

TablePlus is a modern database management tool that provides an intuitive interface for managing databases. To use TablePlus:

1. **Download and Install TablePlus**

   Download TablePlus from the [official website](https://tableplus.com/) and install it on your machine.

2. **Connect to PostgreSQL**

   Connect TablePlus to the PostgreSQL database used by the Flask application. The connection details (host, port, user, password) should be specified in `.env` file.

3. **Explore the Database**

   Use TablePlus to explore the database schema, view data, and perform CRUD operations directly from the interface.

Feel free to use these tools to gain a deeper understanding of how the ASKMEANYTHING application works and to facilitate testing and development.



## Testing

- Run tests using pytest:
    ```bash
    pytest
    ```



## Contributing

- Fork the repository and submit a pull request with a description of your changes.
- Follow best practices for commit messages and use branches if necessary.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
