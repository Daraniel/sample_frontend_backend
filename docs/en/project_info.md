# Simple Frontend Backend

This project is a sample web application built with Flask backend and React frontend.

It allows accessing data from the provided data source (default: excel data file) and accessing various tables on it.

It mainly focuses on creating a relatively generic and easy to extend backend and allows adding a new API endpoint for
each table in a single line. It also auto creates Swagger for the api.

A frontend is provided to allow accessing/viewing the data.

## General Information

This project consists of two parts: a Python Flask backend and a Javascript frontend.

The general design of this project is as follows:

![project_structure_diagram](../project_structure.svg)

In which routing generator creates routing for access data from tables from the data source. Furthermore, the backend is
configurable by a YAML file and has config file validation. Finally, backend has a logger to log various events.

For easy access, the home page of backend shows a list of its APIs. It also has a Swagger UI with relevant API
documentation.

Frontend is a simple single page React page which allows visualization of the data.

## Folder Structure

- `backend`: Contains the backend codebase for the web application. Refer
  to [README.md](../../backend/README.md) in it for setup instructions, or alternatively check the docs.
- `frontend`: Contains the frontend codebase for the web application. Refer
  to [README.md](../../frontend/README.md) in it for setup instructions, or alternatively check the docs.
- `docs`: Contains documentation files providing detailed information about the project setup, configuration, usage, and
  more.

## Getting Started

To learn more about the project:

1. **Backend Setup**: Navigate to the `backend` folder and refer to the [README.md](../../backend/README.md) file in the
   backend folder for instructions on setting up and running the backend.

2. **Frontend Setup**: Navigate to the `frontend` folder and refer to the [README.md](../../frontend/README.md) file in
   the frontend folder for instructions on setting up and running the frontend.

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
