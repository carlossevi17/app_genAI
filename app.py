import streamlit as st
from google import genai

# 1. Configuración visual de la página
st.set_page_config(page_title="FocusAI", page_icon="⚡", layout="centered")

st.markdown("""
    <style>
    .main { opacity: 0.95; }
    stButton>button { width: 100%; border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ FocusAI")
st.caption("Tu asistente personal de aprendizaje y productividad")

# 2. Gestión de la API Key en el lateral
with st.sidebar:
    st.header("Configuración")
    api_key = st.text_input("Introduce tu Gemini API Key:", type="password")
    st.divider()
    st.info("Este asistente utiliza Gemini 2.5 Flash para respuestas instantáneas.")

# 3. Lógica principal
if api_key:
    try:
        client = genai.Client(api_key=api_key)
        
        # Inicializamos el historial de chat si está vacío
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Mostramos los mensajes guardados en la pantalla
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Caja de entrada de texto (Chat Input)
        if prompt := st.chat_input("¿En qué te ayudo hoy?"):
            # 1. Guardar y mostrar el mensaje del usuario
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # 2. Generar respuesta de la IA
            with st.chat_message("assistant"):
                with st.spinner("Pensando..."):
                    # Instrucción de sistema para que sea "inteligente"
                    instruction = "Eres FocusAI, un asistente experto en productividad y síntesis de información. Responde de forma clara, directa y usando formato Markdown para que sea fácil de leer."
                    
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=prompt,
                        config={'system_instruction': instruction}
                    )
                    
                    full_response = response.text
                    st.markdown(full_response)
            
            # 3. Guardar la respuesta de la IA
            st.session_state.messages.append({"role": "assistant", "content": full_response})

    except Exception as e:
        st.error(f"Vaya, algo ha fallado: {e}")
else:
    st.warning("⚠️ Por favor, introduce tu API Key en la barra lateral para comenzar.")
