Perfecto, aquí tienes la estructura organizada para el **Backend** de **RURATEC**, manteniendo la coherencia con el documento anterior:

# 🌱 RURATEC — Backend

## Descripción

Esta es la API REST de **Ruratec**, el motor lógico que permite la conexión entre el campo y el comercio. Se encarga de la gestión de identidades (agricultores y comerciantes), el ciclo de vida de los productos agrícolas, la generación de enlaces de contacto directo vía WhatsApp y la lógica financiera para el procesamiento de pagos, incluyendo el cálculo automático de la comisión del 4% por transacción.

## Integrantes

* Luis Danilo Martinez Cañon
* Andres Felipe Diaz Barbosa
* Hector Ivan Amado Betancur
* Javier Andres Torres Sanchez
* Juan David Ducuara Santa

## Tecnologías utilizadas

* **Lenguaje:** Python 3.x
* **Framework:** Django / Django REST Framework (DRF)
* **Base de datos:** PostgreSQL (Producción) / SQLite (Desarrollo)
* **Librerías principales:**
* **Simple JWT:** Para autenticación segura basada en tokens.
* **CORS Headers:** Para permitir la conexión con el frontend.
* **WhatsApp API Integration:** Para la comunicación entre usuarios.



## Requisitos previos

* **Python** `>= 3.10`
* **pip** (gestor de paquetes de Python)
* **PostgreSQL** instalado y configurado.
* Herramienta para entornos virtuales (`venv`).

## Instalación

1. **Clonar el repositorio:**
```bash
git clone https://github.com/Xavizooo/Backend.git
cd Backend

```


2. **Crear y activar el entorno virtual:**

```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux / Mac
   python3 -m venv venv
   source venv/bin/activate

```

3. **Instalar dependencias:**

```bash
   pip install -r requirements.txt

```

## Ejecución local

1. **Preparar la base de datos:**

```bash
   python manage.py migrate

```

2. **Iniciar el servidor:**
```bash
python manage.py runserver

```



La API será accesible en `http://localhost:8000/api`.

## Base de datos

El sistema está configurado para usar **PostgreSQL**. Debes crear una base de datos llamada `ruratec_db` (o el nombre que prefieras) y configurar las credenciales en el archivo `.env`. Para pruebas rápidas sin configurar Postgres, Django puede utilizar SQLite por defecto si se modifica el `settings.py`.

## Variables de entorno

Crea un archivo `.env` en la raíz con la siguiente información:

```env
SECRET_KEY=tu_clave_secreta
DEBUG=True
DATABASE_URL=postgresql://usuario:password@localhost:5432/ruratec_db
JWT_SECRET_KEY=tu_jwt_secret
COMMISSION_RATE=0.04
WHATSAPP_BASE_URL=https://wa.me/

```

## Usuario de prueba

Para acceder al panel administrativo y gestionar datos iniciales:

1. **Crear superusuario:**
```bash
python manage.py createsuperuser

```


2. **Acceso Admin:** `http://localhost:8000/admin`

## Despliegue

El backend está diseñado para ser desplegado en plataformas como **Render**, **Railway** o **Heroku**.

* Asegúrate de cambiar `DEBUG=False` y configurar los `ALLOWED_HOSTS` con el dominio de producción.

## Evidencias

* **Endpoints de Auth:** Registro y Login con JWT funcionando.
* **CRUD de Productos:** Gestión completa de inventario agrícola.
* **Módulo de Pagos:** Cálculo y registro de transacciones con la comisión aplicada.

```

```
