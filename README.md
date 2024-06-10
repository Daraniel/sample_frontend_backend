# Simple Frontend Backend

This project is a sample web application built with Flask backend and React frontend.

It allows accessing data from the provided data source (default: excel data file) and accessing various tables on it.

It mainly focuses on creating a relatively generic and easy to extend backend and allows adding a new API endpoint for
each table in a single line. It also auto creates Swagger for the api.

A frontend is provided to allow accessing/viewing the data.

## General Information

[Include general information about the project here, such as its purpose, features, and target audience.]

## Folder Structure

- `backend`: Contains the backend codebase for the web application. Refer to [backend/README.md](./backend/README.md)
  for setup instructions.
- `frontend`: Contains the frontend codebase for the web application. Refer
  to [frontend/README.md](./frontend/README.md) for setup instructions.
- `docs`: Contains documentation files providing detailed information about the project setup, configuration, usage, and
  more.

## Getting Started

To learn more about the project:

1. **Backend Setup**: Navigate to the `backend` folder and refer to the [README.md](./backend/README.md) file in the
   backend folder for instructions on setting up and running the backend.

2. **Frontend Setup**: Navigate to the `frontend` folder and refer to the [README.md](./frontend/README.md) file in the
   frontend folder for instructions on setting up and running the frontend.

3. **Documentation**: Explore the `docs` folder for detailed documentation on various aspects of the project, including
   configuration, usage, and more.

## Dockerization

To run the project using Docker, follow these steps:

1. **Build Docker Images**:

    ```bash
    docker-compose build
    ```

2. **Run Docker Containers**:

    ```bash
    docker-compose up
    ```

3. **Access the Application**:

   The frontend will be available at [http://localhost:3000](http://localhost:3000) and the backend
   at [http://localhost:5000](http://localhost:5000).

