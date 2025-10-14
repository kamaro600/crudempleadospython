from app import create_app
import os
import time

app = create_app()

if __name__ == "__main__":
    # Esperar a que la base de datos esté disponible y crear la tabla
    from app.models import Employee

    max_retries = int(os.getenv("DB_WAIT_RETRIES", 10))
    wait_seconds = int(os.getenv("DB_WAIT_SLEEP", 3))

    for attempt in range(1, max_retries + 1):
        try:
            Employee.create_table()
            print("DB lista y tabla creada/asegurada.")
            break
        except Exception as e:
            print(f"DB no lista (intento {attempt}/{max_retries}): {e}")
            time.sleep(wait_seconds)
    else:
        print("Advertencia: no se pudo conectar a la BD tras varios intentos. Arrancando la app igualmente.")

    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)