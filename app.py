from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from mysql.connector import Error
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Configuración de la base de datos
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'cloudcontacts_db'
}

# Conexión a la base de datos
def get_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except Error as e:
        print(f"Error al conectar a la BD: {e}")
        return None

# Página de inicio con formulario
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")

        if not name or not email:
            flash("Nombre y correo son obligatorios", "error")
            return redirect(url_for("index"))

        conn = get_db_connection()
        if not conn:
            flash("Error de conexión a la base de datos", "error")
            return redirect(url_for("index"))

        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO contacts (name, email, phone, created_at) VALUES (%s, %s, %s, %s)",
                (name, email, phone, datetime.now())
            )
            conn.commit()
            flash("Contacto agregado correctamente", "success")
        except mysql.connector.IntegrityError:
            flash("Correo electrónico ya registrado", "error")
        except Exception as e:
            flash(f"Error al guardar contacto: {e}", "error")
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for("index"))

    return render_template("index.html")

# Página de lista de contactos
@app.route("/contacts")
def contacts():
    conn = get_db_connection()
    contacts_list = []
    if not conn:
        flash("Error de conexión a la base de datos", "error")
    else:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM contacts ORDER BY created_at DESC")
        contacts_list = cursor.fetchall()
        cursor.close()
        conn.close()

    return render_template("contacts.html", contacts=contacts_list)


if __name__ == "__main__":
    app.run(debug=True)