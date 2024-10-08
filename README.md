# Proyecto de Django: Backend

Este proyecto está construido con Django, utiliza MySQL y MongoDB para la base de datos.

## Requisitos

- Python 3.7 o superior
- Node.js (para la gestión de dependencias de frontend si es necesario)
- MySQL
- MongoDB

## Configuración del Entorno

1. **Clonar el Repositorio**

   ```bash
   git clone https://github.com/lihuesom/stockFusion.git
   cd stockFusion
   ```

2. **Crear y Activar el Entorno Virtual**

   ```bash
   python3.7 -m venv myenv
   source myenv/bin/activate  # En Windows: myenv\Scripts\activate
   ```

3. **Instalar Dependencias**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar Variables de Entorno**

   Crea un archivo `.env` en la raíz del proyecto y añade las siguientes variables (ajusta según tus necesidades):

   ```env
   CLIENT_MONGODB=
   MONGO_DB=

   DATABASE_NAME=<nombre_de_la_base_de_datos>
   DATABASE_USER=<usuario_de_mysql>
   DATABASE_PASSWORD=<contraseña_de_mysql>
   DATABASE_HOST=localhost
   DATABASE_PORT=3306
   ```

5. **Migraciones y Carga de Datos**

   Ejecuta las migraciones para configurar la base de datos:

   ```bash
   python manage.py migrate
   ```

   Si tienes fixtures de datos, puedes cargarlos con:

   ```bash
   python manage.py loaddata <nombre_del_archivo>
   ```

6. **Ejecutar el Servidor de Desarrollo**

   ```bash
   python manage.py runserver
   ```

## Estructura del Proyecto

- **applications/**: Carpeta que contiene las aplicaciones Django.

  - **inventory/**: Gestión de inventario.
  - **products/**: Gestión de productos.
  - **users/**: Gestión de usuarios.

- **testBankOfBogota/**: Otros componentes específicos del proyecto.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
