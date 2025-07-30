# Acerca del bot 🤖
Este es un chatbot interactivo construido con Streamlit y utiliza la API de Groq, ofreciendo una experiencia de conversación fluida y personalizable con 2 modelos de lenguaje.

## Características Principales
- Conversación Inteligente: Chatea con Ludmi, una asistente de IA amigable y útil.
- Selección de Modelo: Elige entre diferentes modelos de lenguaje de Groq (como Gemma o Llama) para adaptar la experiencia de conversación.
- Historial de Conversación: Visualiza fácilmente el flujo de tu chat.
- Limpiar Conversación: Reinicia la conversación en cualquier momento.
- Interfaz Intuitiva: Diseño limpio y fácil de usar gracias a Streamlit.

## Instalación
```shell 
pip install streamlit 
```
```shell
pip install groq
```
En la carpeta .streamlit:
- Crear un archivo secrets.toml
- Entra a esta página https://groq.com/ consige tu token
- Agrega el token en secrets.toml bajo el nombre de groq_api
Una vez hecho esto abre una terminal dentro del proyecto y escribe lo siguiente
```shell
streamlit run app.py
```

## Tecnologías usadas
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)

Documentación de streamlit y groq
Streamlit: https://docs.streamlit.io/
Groq: https://console.groq.com/docs/overview