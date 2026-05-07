# 🌱 Ruratec — Backend

API REST de **Ruratec**, plataforma que conecta agricultores con comerciantes. Gestiona usuarios, publicación de productos, procesamiento de pagos y el cobro de comisiones del 4% por transacción.

---

## 🚀 Tecnologías

- [Python 3.x](https://www.python.org/)
- [Django](https://www.djangoproject.com/) / [Django REST Framework](https://www.django-rest-framework.org/)
- JWT — Autenticación con tokens
- PostgreSQL / SQLite — Base de datos
- WhatsApp API — Integración para contacto entre usuarios

---

## 📋 Requisitos previos

- Python `>= 3.10`
- pip
- PostgreSQL (para producción) o SQLite (para desarrollo)
- Entorno virtual (`venv` o `virtualenv`)

---

## ⚙️ Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/Xavizooo/Backend.git
cd Backend

# 2. Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate        # Linux / Mac
venv\Scripts\activate           # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
cp .env.example .env
# Editar .env con tus credenciales
```

### Variables de entorno

Crea un archivo `.env` en la raíz del proyecto:

```env
SECRET_KEY=tu_clave_secreta_aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Base de datos
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/ruratec_db

# JWT
JWT_SECRET_KEY=tu_jwt_secret

# Pasarela de pagos
PAYMENT_API_KEY=tu_api_key
COMMISSION_RATE=0.04

# WhatsApp
WHATSAPP_BASE_URL=https://wa.me/
```

---

## ▶️ Ejecución

```bash
# Aplicar migraciones
python manage.py migrate

# Crear superusuario (admin)
python manage.py createsuperuser

# Correr el servidor de desarrollo
python manage.py runserver
```

La API estará disponible en `http://localhost:8000/api`.

El panel de administración estará en `http://localhost:8000/admin`.

---

## 🗂️ Estructura del proyecto

```
Backend/
├── ruratec/             # Configuración principal del proyecto Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/               # App de usuarios (agricultores y comerciantes)
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── products/            # App de productos agrícolas
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── payments/            # App de pagos y comisiones
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── requirements.txt
└── manage.py
```

---

## 📡 Endpoints principales

### Autenticación
| Método | Endpoint | Descripción |
|---|---|---|
| `POST` | `/api/auth/register/` | Registro de nuevo usuario |
| `POST` | `/api/auth/login/` | Inicio de sesión, retorna JWT |
| `POST` | `/api/auth/refresh/` | Renovar token de acceso |

### Usuarios
| Método | Endpoint | Descripción |
|---|---|---|
| `GET` | `/api/users/me/` | Perfil del usuario autenticado |
| `PUT` | `/api/users/me/` | Actualizar perfil |

### Productos
| Método | Endpoint | Descripción |
|---|---|---|
| `GET` | `/api/products/` | Listar todos los productos |
| `POST` | `/api/products/` | Publicar nuevo producto (agricultor) |
| `GET` | `/api/products/{id}/` | Detalle de un producto |
| `PUT` | `/api/products/{id}/` | Editar producto |
| `DELETE` | `/api/products/{id}/` | Eliminar producto |

### Pagos
| Método | Endpoint | Descripción |
|---|---|---|
| `POST` | `/api/payments/checkout/` | Iniciar pago de una transacción |
| `GET` | `/api/payments/history/` | Historial de pagos del usuario |

> La comisión del **4%** se aplica automáticamente en cada transacción procesada.

---

## ✨ Funcionalidades principales

- **Registro por rol** — Usuarios se registran como agricultor o comerciante
- **Gestión de productos** — CRUD completo de productos con fotos, precio y descripción
- **Integración WhatsApp** — Generación de enlace directo para contactar al agricultor
- **Procesamiento de pagos** — Flujo de pago con comisión del 4% aplicada automáticamente
- **Autenticación JWT** — Tokens de acceso seguros con expiración y refresh

---

## 🔗 Conexión con el Frontend

Este backend es consumido por el frontend de Ruratec.

- Repositorio del frontend: [https://github.com/Xavizooo/frontend-proyecto](https://github.com/Xavizooo/frontend-proyecto)
- CORS configurado para `http://localhost:3000` en desarrollo

---

## 🤝 Contribuciones

1. Haz fork del repositorio
2. Crea una rama: `git checkout -b feature/nueva-funcionalidad`
3. Haz commit de tus cambios: `git commit -m 'feat: descripción del cambio'`
4. Push a tu rama: `git push origin feature/nueva-funcionalidad`
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT.
