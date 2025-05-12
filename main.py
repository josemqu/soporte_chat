import os
import json
from typing import AsyncGenerator
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import AsyncOpenAI

# Cargar variables de entorno
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Inicializar cliente OpenAI asíncrono
client = AsyncOpenAI(api_key=api_key)
app = FastAPI()

# Montar carpeta estática
app.mount("/static", StaticFiles(directory="./static"), name="static")

# Base de conocimiento
with open('knowledge_base.json') as f:
    knowledge_base = json.load(f)

# Modelo de entrada
typing_app = BaseModel
class UserQuery(BaseModel):
    mensaje: str

@app.get('/')
async def root():
    return FileResponse('static/index.html')

@app.post('/chat/stream')
async def chat_stream(query: UserQuery):
    # Construir prompt para respuesta en lenguaje natural
    prompt = f"""
Sos un asistente técnico especializado. A partir del mensaje del usuario:
"{query.mensaje}"

1. Identificá la aplicación afectada (ej: Corva, WellExpert, RigCloud).
2. Clasificá el tipo de problema (acceso, visualización, error, conexión, etc.).
3. Proporcioná una respuesta en lenguaje natural, indicando claramente qué contacto debe comunicarse y cómo.

En una oración breve, devuelve al usuario indicando a qué contacto debe realizar la consulta.
Si detectas que hay una consulta y además esa consulta no esta relacionada con nada de lo que se encuentra en la base de conocimiento, simplemente responde que lamentablemente no puedes ayudar con esa consulta especifica. Sin embargo, si puedes inferir que se trata de una consulta relacionada con algún incidente de sistemas informáticos, recomienda realizar la consulta a la mesa de soporte de Tecpetrol.
Sé amable respondiendo a frases de agradecimiento y a saludos de bienvenida o despedida.

Usá esta base de conocimiento para derivar el contacto:
{json.dumps(knowledge_base, indent=2)}
"""

    async def generate() -> AsyncGenerator[str, None]:
        response = await client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            stream=True
        )
        # Streamear directamente la respuesta en lenguaje natural
        async for chunk in response:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

    return StreamingResponse(generate(), media_type='text/event-stream')