# 🐾 Pet Manager Desktop App

Aplicación de escritorio para la gestión de mascotas desarrollada con Python.
El sistema permite registrar, consultar, actualizar y eliminar mascotas, además de visualizar estadísticas y gráficos sobre la información almacenada.

Este proyecto fue desarrollado como práctica de arquitectura modular, uso de servicios y construcción de interfaces gráficas profesionales.

---

# 🎥 Demo del proyecto

📺 Video demostración del funcionamiento del sistema:

(Agrega aquí el link de tu video de demostración cuando lo subas)

Ejemplo:

https://youtube.com/tu-video-demo

---

# 🚀 Características principales

✔ Registro de mascotas
✔ Edición de información de mascotas
✔ Eliminación de registros
✔ Panel de estadísticas del sistema
✔ Visualización de datos mediante gráficos
✔ Tabla interactiva con ordenamiento
✔ Búsqueda en tiempo real
✔ Paginación de registros
✔ Arquitectura modular escalable

---

# 🖥️ Tecnologías utilizadas

Este proyecto utiliza las siguientes tecnologías:

* Python
* PySide6 (interfaz gráfica)
* SQLAlchemy (ORM)
* SQLite (base de datos)
* Matplotlib (visualización de datos)

---

# 🏗️ Arquitectura del proyecto

El proyecto sigue una arquitectura modular organizada por capas:

```
pyside_mascotas
│
├── database
│   └── connection.py
│
├── models
│   └── mascota.py
│
├── services
│   └── mascota_service.py
│
├── views
│   └── home_view.py
│
├── app.py
```

Cada capa tiene una responsabilidad específica.

### Models

Define las entidades de la base de datos.

### Services

Contiene la lógica de negocio y comunicación con la base de datos.

### Views

Maneja la interfaz gráfica del usuario.

### Database

Administra la conexión con la base de datos.

---

# 📊 Sistema de estadísticas

El sistema incluye un panel que muestra información en tiempo real sobre los registros almacenados.

Las estadísticas calculadas incluyen:

* Total de mascotas registradas
* Peso promedio de las mascotas
* Número de especies diferentes registradas

Estas métricas se obtienen mediante consultas agregadas usando SQLAlchemy.

---

# 📈 Visualización de datos (Gráficas)

La aplicación integra gráficos dinámicos utilizando Matplotlib.

El sistema genera un gráfico de barras que muestra:

* Cantidad de mascotas por especie

Este gráfico permite visualizar rápidamente la distribución de especies registradas en el sistema.

Flujo de funcionamiento:

1. El usuario presiona el botón **"Ver gráfica de especies"**
2. El sistema consulta los datos agrupados en la base de datos
3. Se generan las etiquetas y valores
4. Matplotlib construye el gráfico
5. El gráfico se muestra en una ventana independiente

Esto permite transformar datos almacenados en información visual útil.

---

# 🔎 Funcionalidades de la tabla

La tabla de mascotas permite:

* Ordenar columnas
* Seleccionar registros
* Filtrar resultados mediante búsqueda
* Navegar entre páginas de registros

Estas funciones permiten manejar grandes cantidades de información de forma eficiente.

---

# ⚙️ Instalación del proyecto

1. Clonar el repositorio

```
git clone https://github.com/tu-usuario/pyside_mascotas.git
```

2. Entrar a la carpeta del proyecto

```
cd pyside_mascotas
```

3. Crear entorno virtual

```
python -m venv venv
```

4. Activar entorno virtual

Windows

```
venv\Scripts\activate
```

5. Instalar dependencias

```
pip install -r requirements.txt
```

6. Ejecutar aplicación

```
python app.py
```

---

# 📦 Dependencias principales

El proyecto utiliza las siguientes librerías:

```
PySide6
SQLAlchemy
Matplotlib
```

---

# 🧠 Conceptos aplicados

Durante el desarrollo se aplicaron los siguientes conceptos de ingeniería de software:

* Arquitectura por capas
* Separación de responsabilidades
* Programación orientada a objetos
* ORM para gestión de base de datos
* Interfaces gráficas con Qt
* Visualización de datos
* Modularización del código

---

# 📌 Posibles mejoras futuras

El sistema puede ampliarse con nuevas funcionalidades:

* Sistema de autenticación de usuarios
* Exportación de datos a Excel o PDF
* Panel administrativo avanzado
* Gráficas adicionales
* Generación de reportes
* Sistema de respaldo automático de base de datos

---

# 👨‍💻 Autor

Desarrollado por:

William Alape Rivera

Estudiante de desarrollo de software interesado en:

* desarrollo backend
* aplicaciones de escritorio
* arquitectura de software
* visualización de datos

---

# 📄 Licencia

Este proyecto fue desarrollado con fines educativos y de portafolio.
