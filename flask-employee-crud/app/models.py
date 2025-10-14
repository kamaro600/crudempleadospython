from .db import get_connection


class Employee:
    def __init__(self, username, name, email, job_position):
        self.username = username
        self.name = name
        self.email = email
        self.job_position = job_position

    def __repr__(self):
        return f"<Employee {self.username}>"
    
    @staticmethod
    def create_table():
        sql = """
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(80) NOT NULL UNIQUE,
            name VARCHAR(120) NOT NULL,
            email VARCHAR(120) NOT NULL UNIQUE,
            position VARCHAR(120) NOT NULL
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """
        conn = get_connection()
        with conn:
            with conn.cursor() as cur:
                cur.execute(sql)

    @classmethod
    def all(cls):
        conn = get_connection()
        with conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM employees ORDER BY id")
                return cur.fetchall()

    @classmethod
    def get(cls, id):
        conn = get_connection()
        with conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM employees WHERE id=%s", (id,))
                return cur.fetchone()

    @classmethod
    def create(cls, username, name, email, position):
        conn = get_connection()
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO employees (username, name, email, position) VALUES (%s,%s,%s,%s)",
                    (username, name, email, position)
                )
                return cls.get(cur.lastrowid)

    @classmethod
    def update(cls, id, username, name, email, position):
        conn = get_connection()
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE employees SET username=%s, name=%s, email=%s, position=%s WHERE id=%s",
                    (username, name, email, position, id)
                )
                return cls.get(id)

    @classmethod
    def delete(cls, id):
        conn = get_connection()
        with conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM employees WHERE id=%s", (id,))
                return cur.rowcount > 0