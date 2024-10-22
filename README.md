# 🛡️ Ciberseguridad Comentarios

¡Bienvenido al proyecto **Ciberseguridad Comentarios**! 🎉 Este proyecto es una aplicación web creada con **FastAPI** que permite a los usuarios compartir sus opiniones sobre ciberseguridad. Los comentarios se almacenan y se pueden visualizar en la interfaz de la página. Además, el diseño es atractivo, con un fondo animado y elementos interactivos. 🌐🔒

## 🌐 Cómo Visualizar mi página
https://mi-fastapiciberseguridad-production.up.railway.app/

## 📸 Capturas de Pantalla

### Página Principal
![image](https://github.com/user-attachments/assets/944a6e20-3b28-4b1e-b05f-cd6da96aded6)

![image](https://github.com/user-attachments/assets/1b071eb8-efe9-426c-92a8-9150526120bb

![image](https://github.com/user-attachments/assets/7006fe28-ee34-48ac-9fa3-924d40bbac9d)




## 📋 Descripción del Proyecto
Esta aplicación está destinada a fomentar discusiones sobre la importancia de la ciberseguridad. Los usuarios pueden:
- 📣 Agregar sus opiniones sobre ciberseguridad.
- 👀 Ver todos los comentarios disponibles.
- 📄 Visualizar los comentarios en formato JSON.

La aplicación usa **FastAPI** en el backend, junto con **HTML**, **CSS** y **JavaScript** en el frontend.

## 🚀 Instalación y Configuración
Sigue estos pasos para configurar el proyecto en tu máquina local:

### 1. Clonar el Repositorio
```bash
$ git clone https://github.com/tu-usuario/ciberseguridad-comentarios.git
$ cd ciberseguridad-comentarios
```

### 2. Crear un Entorno Virtual
Es recomendable crear un entorno virtual para gestionar las dependencias:
```bash
$ python -m venv venv
$ source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar las Dependencias
Instala las dependencias listadas en el archivo `requirements.txt`:
```bash
$ pip install -r requirements.txt
```

### 4. Ejecutar la Aplicación
Inicia la aplicación ejecutando el siguiente comando:
```bash
$ uvicorn main:app --reload
```
La aplicación estará disponible en [http://127.0.0.1:8000](http://127.0.0.1:8000) 🚀.

## 📂 Estructura del Proyecto
```
├── main.py                 # Código principal del backend (FastAPI)
├── requirements.txt        # Dependencias del proyecto
├── static
│   ├── style.css           # Archivo de estilo CSS
│   ├── hacker.jpg          # Imagen del favicon
│   └── cyberseguridad.jpg  # Imagen principal de la página
├── templates
│   └── index.html          # Plantilla HTML para la interfaz
└── README.md               # Este archivo
```

## 🌟 Características
- 📝 **Agregar Comentarios**: Los usuarios pueden agregar sus opiniones sobre ciberseguridad usando un formulario interactivo.
- 🔄 **Ver Comentarios Actualizados**: Los comentarios se muestran automáticamente en la página después de ser agregados.
- 📊 **Visualización JSON**: Muestra todos los comentarios en formato JSON.
- 🎨 **Diseño Atractivo**: Animaciones de fondo y botones interactivos para una mejor experiencia de usuario.

## 📦 Dependencias
Las dependencias principales del proyecto son:
- **FastAPI**: Framework para construir APIs rápidas y eficientes.
- **Uvicorn**: Servidor ASGI para ejecutar la aplicación.
- **Jinja2**: Motor de plantillas para la generación de páginas HTML.

## 🛠️ Cómo Contribuir
¡Las contribuciones son bienvenidas! Si deseas contribuir:
1. Haz un fork del proyecto 🍴.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`) 🌿.
3. Haz commit de tus cambios (`git commit -m 'Agrega nueva característica'`) 💬.
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`) 🚀.
5. Abre un Pull Request 📥.

## 🌐 Cómo Visualizar mi repositorio
Puedes visualizar mi PÁGINA en línea visitando el siguiente enlace https://github.com/RominaAguirreVelazco-0305/Mi_-FastAPI_Ciberseguridad.git

## ✍️ Autor
- Romina Jacqueline Aguirre Velazco
- 📧 romina.aguirre8841@alumnos.udg.mx
- Desarrollado con ❤️ por Romina Aguirre. 

¡Gracias por visitar el proyecto! Esperamos que encuentres útil esta aplicación y puedas contribuir con tus opiniones sobre ciberseguridad. 🔐✨
