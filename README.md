# CRUD EMPLEADOS PYTHON -MYSQL
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
- Docker
- Flask
- PyMySQL
- MySQL Server

# Instrucciones

1. Clonar el repository:
   ```
   git clone https://github.com/kamaro600/crudempleadospython.git
   cd crudempleadospython
   cd flask-employee-crud
   ```

2. Instalar los paquetes requeridos:
   ```
   pip install -r requirements.txt
   ```

3. Construir la aplicacion usando docker:
   ```
   docker-compose up --build
   ```

4. Accede a la aplicacion en `http://localhost:5000`.


