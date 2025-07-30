import streamlit as st
from groq import Groq
import os

st.set_page_config(page_title="ChatBot IA", page_icon="img/img2.png", layout="centered")
st.title("ChatBot IA")

try:
    groq_api_key = st.secrets["groq_api"]
except KeyError:
    st.error("La clave 'groq_api' no se encontró en st.secrets. Asegúrate de configurarla.")
    st.stop()

@st.cache_resource
def get_groq_client(api_key):
    return Groq(api_key=api_key)

client = get_groq_client(groq_api_key)


if "usuario" not in st.session_state:
    st.session_state.usuario = ""
if "logueado" not in st.session_state:
    st.session_state.logueado = False
if "mensajes" not in st.session_state:
    st.session_state.mensajes = [
        {"role": "system", "content": "Eres una asistente amigable llamada Ludmi."}
    ]


if not st.session_state.logueado:
    st.header("¡Bienvenido soy :violet[Ludmi]!")
    st.write("Para empezar, por favor dinos tu nombre.")
    nombre = st.text_input("Tu nombre:", key="nombre_input_login")
    if st.button("Ingresar al Chat", key="login_button"):
        if nombre.strip():
            st.session_state.usuario = nombre.strip()
            st.session_state.logueado = True
            st.success(f"¡Hola, {st.session_state.usuario}! Estoy lista para ayudarte.")
            st.rerun()
        else:
            st.warning("Por favor, ingresa tu nombre para continuar.")
else:
    st.subheader(f"Hola {st.session_state.usuario}, ¿en qué puedo ayudarte hoy?")

    with st.sidebar:
        st.header("Configuración del Chat")
        
        modelos = ['gemma2-9b-it', 'llama-3.1-8b-instant']
        modelo_seleccionado = st.selectbox("Selecciona un modelo de IA", modelos, index=modelos.index(st.session_state.get('modelo_seleccionado', 'gemma2-9b-it')), key="model_selector")
        st.session_state.modelo_seleccionado = modelo_seleccionado

        st.markdown("---")

        if st.button("Limpiar Conversación", key="clear_chat_button", help="Borra todo el historial de mensajes."):
            st.session_state.mensajes = [
                {"role": "system", "content": "Eres una asistente amigable llamada Ludmi."}
            ]
            st.success("Conversación limpiada. ¡Empecemos de nuevo!")
            st.rerun()

        st.markdown("---")
        st.info("💡 **Consejo:** Puedes seleccionar un modelo diferente en cualquier momento.")

    for msg in st.session_state.mensajes:
        if msg["role"] == "system":
            continue
        
        if msg["role"] == "user":
            with st.chat_message("user", avatar="img/img1.png"):
                st.markdown(msg["content"])
        elif msg["role"] == "assistant":
            with st.chat_message("assistant", avatar="img/img2.png"):
                st.markdown(msg["content"])

    pregunta_usuario = st.chat_input("Escribe tu pregunta aquí...", key="chat_input_main")

    if pregunta_usuario:
        st.session_state.mensajes.append({"role": "user", "content": pregunta_usuario.strip()})
        
        with st.chat_message("user", avatar="img/img1.png"):
            st.markdown(pregunta_usuario.strip())

        try:
            with st.spinner("Ludmi está pensando..."):
                messages_for_llm = [
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.mensajes
                ]
                
                answer = client.chat.completions.create(
                    model=st.session_state.modelo_seleccionado,
                    messages=messages_for_llm,
                    temperature=0.7,
                    max_tokens=1024
                )
                content_answer = answer.choices[0].message.content
                
                st.session_state.mensajes.append({"role": "assistant", "content": content_answer})
                
                with st.chat_message("assistant", avatar="img/img2.png"):
                    st.markdown(content_answer)
                
        except Exception as e:
            st.error(f"¡Ups! Ocurrió un error al comunicarse con Ludmi: {e}")
            if st.session_state.mensajes[-1]["role"] == "user":
                st.session_state.mensajes.pop()
            st.warning("Por favor, intenta tu pregunta de nuevo o verifica tu conexión.")
