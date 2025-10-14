from flask import current_app
import os
import pymysql.cursors

def get_connection():
    host = os.getenv("DB_HOST", "db")
    port = int(os.getenv("DB_PORT", 3306))
    user = os.getenv("DB_USER", "root")
    password = os.getenv("DB_PASSWORD", os.getenv("DB_ROOT_PASSWORD", "password"))
    db = os.getenv("DB_NAME", "employees_db")
    return pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=db,
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True,
        charset="utf8mb4"
    )

def execute_query(query, args=None):
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(query, args)
            connection.commit()

def fetch_all(query, args=None):
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(query, args)
            return cursor.fetchall()

def fetch_one(query, args=None):
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(query, args)
            return cursor.fetchone()