# Frontend Documentation

## Overview

The `Tablee` component is the main React component in this app which fetches and displays data in a table format. It
allows users to select different tables and data levels to view corresponding data. This component uses Axios for data
fetching and Material UI for styling along with Bootstrap for layout.

Although it is common to use to manage the application state, since this project is pretty simple, it was written
without it.

## Component Structure

### State Variables

- `level`: Represents the selected data level (default: `"1"`).
- `table`: Represents the selected table (default: `"bruftoinlandsprodukt_in_jeweiligen_preisen"`).
- `data`: Stores the fetched data for the selected table and level.
- `metadata`: Stores metadata information for the selected table.

### Effects

1. **Fetch Data**:
    - Fetches data from the API based on the selected `table` and `level`.
    - Parses the response and updates the `data` state.

2. **Fetch Metadata**:
    - Fetches metadata from the API based on the selected `table`.
    - Parses the response and updates the `metadata` state.

## Key Features

- **Dynamic Table and Level Selection**: The `TableDrop` and `LevelDrop` components allow users to select different
  tables and levels dynamically.
- **Metadata Display**: Displays metadata information at the top of the table.
- **Scrollable Table**: The table is scrollable for easier navigation of large datasets.
- **Sorted Headers**: Headers are sorted to display string-based headers first.

## Error Handling

- Both `useEffect` hooks contain error handling to log any issues encountered during data fetching to the console.
