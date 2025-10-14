# CRUD EMPLEADOS
Este proyecto es un crud simple para manejo de empleados con Flask, Bootstrap y MYSQL. 

## Features

- Administracion de empleados con campos de usuario, nombre , email y cargo.
- Interfaz con bootstrap
- Aplicacion dockerizada

## Estructura del proyecto

```
flask-employee-crud
├── app
│   ├── __init__.py
│   ├── config.py
│   ├── db.py
│   ├── models.py
│   ├── routes.py
│   ├── templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── create.html
│   │   ├── edit.html
│   │   └── detail.html
│   └── static
│       └── css
│           └── styles.css
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── run.py
├── .env.example
└── README.md
```

## Requisitos

- Python 3.x
- Flask
- PyMySQL
- MySQL Server

# Instrucciones

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-employee-crud
   ```

2. Create a `.env` file based on the `.env.example` file and configure your database connection settings.

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Build and run the application using Docker:
   ```
   docker-compose up --build
   ```

5. Access the application at `http://localhost:5000`.

## Usage

- Navigate to the home page to view the list of employees.
- Use the "Create Employee" button to add a new employee.
- Click on an employee's name to view their details.
- Use the "Edit" button to update employee information.
- Use the "Delete" button to remove an employee record.

## License

This project is licensed under the MIT License.
