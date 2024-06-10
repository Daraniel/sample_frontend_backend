# Frontend Displaying the Data as a Dynamic Table

## Overview

This folder contains a web application built using React.js that allows users to fetch and display data from an API in a
tabular format. It leverages the Axios library for API requests and provides a user-friendly interface for selecting
different tables and levels of data.

Although it is common to use to manage the application state, since this project is pretty simple, it was written
without it.

Please refer to the docs folder for indepth details about this project.

## Features

- **Dynamic Table and Level Selection**: Users can choose from a list of available tables and levels to fetch specific
  data from the API.

- **Metadata Display**: Metadata information for the selected table is displayed at the top of the table, providing
  additional context for the data being viewed.

- **Sortable Headers**: The table headers are sorted to display string-based headers first, improving readability and
  user experience.

- **Scrollable Table**: The table is made scrollable to accommodate large datasets, ensuring ease of navigation and
  exploration.

## Usage

### Installation

1. Clone the repository: `git clone https://github.com/Daraniel/sample_frontend_backend/`
2. Navigate to the frontend directory: `cd frontend`
3. Install dependencies: `npm install`

### Running the App

- Start the development server: `npm start`
- Open [http://localhost:3000](http://localhost:3000) in your browser to view the app.

## Main Dependencies

- React.js
- Axios
- Bootstrap
- Material UI
