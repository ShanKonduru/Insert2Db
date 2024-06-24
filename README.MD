# insert2db Program

## Overview
insert2db is a Python program designed to read data from CSV and Excel files and insert it into a database (PostgreSQL, Oracle, etc.) using object-oriented principles and secure handling of database credentials.

## Features
Supports CSV and Excel (XLS/XLSX) file formats.
Modular database handlers (PostgreSQLHandler, OracleHandler) for different database connections.
Uses environment variables or configuration files to securely manage database credentials.
Handles table creation and data insertion based on file name conventions.

## Prerequisites
Before running insert2db, ensure you have the following installed:

Python 3.x (https://www.python.org/downloads/)
Necessary Python packages (pandas, cx_Oracle, psycopg2)

## Installation
Clone the repository:

``` bash
git clone https://github.com/shankonduru/insert2db.git
cd insert2db
```

## Install dependencies:

```bash
Copy code
poetry install
```
Set up environment variables or create a config.ini file with database credentials (see Configuration section).

## Configuration

### Environment Variables

Set the following environment variables with your database credentials:

DB_NAME: Name of your database
DB_USERNAME: Database username
DB_PASSWORD: Database password
DB_HOST: Database host (e.g., localhost)
DB_PORT: Database port (e.g., 5432 for PostgreSQL)

## Configuration File (config.ini)

Alternatively, you can create a config.ini file in the project directory with the following format:

```ini
[database]
    dbname = your_database
    user = your_username
    password = your_password
    host = your_host
    port = your_port
```

Replace your_database, your_username, your_password, your_host, and your_port with your actual database connection details.

## Usage

Run the runme.py script to insert data into the database:

```bash
poetry run python runme.py
```

### Notes
Ensure that your CSV or Excel file is placed in the appropriate directory (path/to/your/file.csv or path/to/your/file.xlsx).
The program will create a table in the database using the file name as the table name (for CSV files) or <filename>_<sheetname> (for Excel files).
Data will be inserted into the respective table in the database.

### Troubleshooting
If you encounter any issues, ensure that Python and required packages are properly installed.
Double-check database credentials and file paths.
Review database logs for any specific errors related to connections or queries.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

