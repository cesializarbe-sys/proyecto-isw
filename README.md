# CloudContacts

**Cesia Belén Lizarbe Mesajil**
**Tutor:** Ebert Bernardo Ocares Luna

## Creación y configuración de instancias EC2

Para iniciar el proyecto, se crearon dos instancias EC2 en AWS con sistema operativo Ubuntu. Se configuraron los puertos necesarios, específicamente el puerto 80 para HTTP y el puerto 22 para SSH, a través del grupo de seguridad. Posteriormente, se generó y descargó la clave SSH para poder conectarnos a las instancias de forma segura. Además, se asignó una **IP elástica** a la instancia principal para poder acceder al servidor de manera constante desde cualquier lugar.

La conexión a la instancia se realizó mediante SSH usando la clave descargada y la dirección IP de la instancia principal.

## Creación del proyecto CloudContacts

En **Visual Studio Code** se creó la estructura inicial del proyecto, incluyendo todos los archivos necesarios para la conexión a la base de datos y la configuración del entorno virtual. Se instaló **Tailwind CSS v4**, generando el archivo `output.css` para utilizarlo en el diseño de la interfaz. Esto permitió que la aplicación tenga un aspecto moderno y sea **responsive**, adaptable a diferentes tamaños de pantalla.

## Instalación del entorno y clonación del repositorio

Se actualizó el sistema operativo de la instancia para evitar problemas de compatibilidad, y se instalaron las herramientas necesarias como Git, Python y pip. Después, se clonó el repositorio del proyecto desde GitHub y se creó un **entorno virtual** para gestionar las dependencias del proyecto de manera aislada. Dentro del entorno virtual se instalaron todos los paquetes listados en el archivo `requirements.txt`.

## Configuración de Flask y puerto 5000

Para poder ejecutar la aplicación Flask desde la instancia EC2 y acceder a ella desde un navegador externo, fue necesario abrir el puerto 5000 en el grupo de seguridad de AWS. Esto se hizo agregando una regla personalizada que permitiera conexiones TCP desde cualquier dirección.

Además, en el archivo `app.py` se configuró Flask para que escuche desde cualquier dirección IP, permitiendo que el servidor sea accesible desde fuera de la instancia.

## Instalación y configuración de MySQL

En la instancia que se utilizó como servidor de base de datos, primero se actualizó el sistema y luego se instaló **MySQL Server**. Para permitir conexiones remotas desde la instancia de Flask, se modificó el archivo de configuración de MySQL (`mysqld.cnf`), cambiando la línea `bind-address` de `127.0.0.1` a `0.0.0.0`. Esto hizo posible que otras instancias o aplicaciones se conecten a la base de datos de forma segura.

Se creó la base de datos `cloudcontacts_db` y un usuario específico con permisos para conectarse desde la IP privada de la instancia de Flask. Finalmente, se instalaron las librerías necesarias en Python para que Flask pueda interactuar con MySQL, incluyendo `mysqlclient`.

## Creación de la tabla y configuración del archivo `.env`

Desde la instancia de Flask se realizó la conexión remota a la base de datos y se ejecutó el script SQL para crear la tabla `contacts`. Además, se configuró el archivo `.env` con las credenciales y parámetros de conexión, incluyendo la clave secreta de Flask, host, puerto, usuario, contraseña y nombre de la base de datos.

Una vez configurado, se verificó que Flask estuviera corriendo correctamente y que los datos se almacenaran correctamente en la tabla `contacts`. También se comprobó que la aplicación fuera completamente **responsive**, funcionando correctamente en distintos dispositivos.
