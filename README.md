# Chat Agéntico Completo (Fantasía)

Este proyecto implementa un chat de soporte operativo especializado en plataformas ficticias (Applix, Dataflow, WellTrack), usando FastAPI y la API de OpenAI con streaming.

---

## 📂 Estructura del proyecto

```
chat-app/
├── main.py             # Backend en FastAPI y streaming
├── knowledge_base.json # Base de conocimiento ficticia para derivar contactos
├── static/
│   └── index.html      # Interfaz web moderna
├── .env                # Variables de entorno (API Key de OpenAI)
└── requirements.txt    # Dependencias Python
```

---

## 🔧 Requisitos previos

- Python 3.8 o superior
- Clave de API de OpenAI válida
- (Opcional) Entorno virtual para Python

---

## ⚙️ Instalación y ejecución

1. **Clonar el repositorio**

   ```bash
   git clone https://github.com/tu-usuario/chat-app.git
   cd chat-app
   ```

2. **Crear y activar un entorno virtual** (recomendado)

   ```bash
   python -m venv venv
   # Linux / macOS
   source venv/bin/activate
   # Windows
   venv\Scripts\activate
   ```

3. **Instalar dependencias**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**  
   Crea un archivo `.env` en la raíz del proyecto con:

   ```ini
   OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```

5. **Iniciar el servidor FastAPI**

   ```bash
   uvicorn main:app --reload
   ```

6. **Abrir la interfaz en el navegador**  
   Visita:
   ```
   http://localhost:8000/
   ```

---

## 🧑‍💻 Uso

- Escribe tu mensaje en el campo inferior y presiona **Enviar** o **Enter**.
- La conversación aparece en burbujas: tus mensajes en color primario y las respuestas del bot en color de fondo claro.
- La respuesta del bot llega en tiempo real gracias al streaming de la API.

---

## 📖 Personalización

- **Base de conocimiento**  
  Edita `knowledge_base.json` para cambiar nombres de aplicaciones y contactos ficticios.

- **Estilos**  
  Ajusta colores, fuentes y diseño en `static/index.html`.

- **Parámetros de la API**  
  En `main.py` puedes cambiar:
  - Modelo (`model`)
  - Temperatura (`temperature`)
  - Otros parámetros del método `client.chat.completions.create`

---

## 📚 Referencias

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [FastAPI StreamingResponse](https://fastapi.tiangolo.com/advanced/custom-response/)

---

> **Tip:** Para despliegue en producción, considera usar Uvicorn con Gunicorn y un proxy inverso (Nginx), además de gestionar las variables de entorno de forma segura.
