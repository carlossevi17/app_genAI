import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="Falla San Ramón 2026", page_icon="🔥", layout="centered")

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    .main { background-color: #fff5e6; }
    .stButton>button { background-color: #ff4b4b; color: white; border-radius: 20px; }
    h1 { color: #d32f2f; text-shadow: 2px 2px #feb236; }
    .fallera-card { text-align: center; padding: 10px; border: 1px solid #ddd; border-radius: 10px; background: white; }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA Y CUENTA ATRÁS ---
st.title("🔥 Falla San Ramón: ¡Fuego y Tradición!")

# Cálculo de días para el 19 de Marzo de 2026
fecha_crema = datetime(2026, 3, 19)
dias_faltan = (fecha_crema - datetime.now()).days

col_head1, col_head2 = st.columns([2, 1])
with col_head1:
    st.subheader("La falla con más 'sentit' de todo el barrio")
with col_head2:
    st.metric(label="Días para la Cremà", value=f"{dias_faltan} ⏳")

st.markdown("---")

# --- NUEVA SECCIÓN: CUADRO DE HONOR ---
st.header("👑 Nuestras Representantes")
col_fm1, col_fm2 = st.columns(2)
fecha_crida2 = datetime(2026, 2, 22)
dias_faltan2 = (fecha_crida2 - datetime.now()).days

with col_fm1:
    st.markdown('<div class="fallera-card">', unsafe_allow_html=True)
    st.image("https://www.hellovalencia.es/wp-content/uploads/2023/10/Falleras-Mayores-2024.jpeg", caption="Fallera Mayor: Sofía García y Lucía Nieto")
    st.markdown('</div>', unsafe_allow_html=True)

with col_fm2:
    st.metric(label="Días para la Cridà", value=f"{dias_faltan2} ⏳")

st.markdown("---")

# --- SECCIÓN: EL MONUMENTO ---
col1, col2 = st.columns([2, 1])
with col1:
    st.header("🎭 Lema 2026: 'El Despertar del Drac'")
    st.write("Con un remate de **15 metros**, el Drac escupirá fuego real.")
    st.info("**Artista:** Manolo 'El Chispas' | **Sección:** Especial")
with col2:
    st.image("https://img.freepik.com/fotos-premium/boceto-dragon-tres-cabezas-palabra-dragon-frente_902846-4103.jpg")

st.markdown("---")

# --- RESERVA DE COMIDAS ---
st.header("🍽️ Apuntarse a la Comilona")
apellidos_ejemplo = ["García Martínez", "Rodríguez Sánchez", "López Pérez", "González Fernández", "Ruiz Jiménez", "Serrano Cano", "Ramírez Vidal", "Morales Ortiz", "Navarro Soler", "Blanco Ferrer"]

with st.form("form_comidas"):
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        familia = st.selectbox("Familia / Nombre", options=apellidos_ejemplo)
        dia = st.selectbox("Día", ["15 Marzo", "16 Marzo", "17 Marzo", "18 Marzo", "19 Marzo"])
    with col_f2:
        tipo_comida = st.multiselect("¿A qué te apuntas?", ["Almuerzo", "Comida", "Cena"])
        comensales = st.number_input("Nº de personas", min_value=1, max_value=20, value=2)
    submit = st.form_submit_button("Confirmar Asistencia")

if submit:
    st.success(f"✅ ¡Apuntado! La familia {familia} vendrá el {dia}. ¡Traed hambre!")

st.markdown("---")

# --- NUEVA SECCIÓN: MURO DE LA COMISIÓN ---
st.header("💬 El Muro Fallero")
with st.expander("Ver mensajes o dejar uno"):
    nombre_muro = st.text_input("Tu nombre")
    mensaje = st.text_area("¿Qué quieres decirle a la falla?")
    if st.button("Publicar mensaje"):
        st.toast(f"¡Gracias {nombre_muro}, mensaje enviado!")
        st.write(f"**{nombre_muro}**: {mensaje}")

st.markdown("---")

# --- AGENDA, MASCLETÓMETRO Y CARPA ---
# (Mantengo tus secciones pero compactas para que no sea eterno)
st.header("📅 Agenda de la Semana")
agenda = {"Día": ["15 Marzo", "16 Marzo", "17 Marzo", "18 Marzo", "19 Marzo"], "Evento": ["La Plantà", "Reparto de Buñuelos", "Ofrenda de Flores", "Nit del Foc", "La Cremà"], "Hora": ["08:00", "11:00", "16:00", "23:59", "22:00"]}
st.table(pd.DataFrame(agenda))

st.header("🧨 El Mascletómetro")
if st.button("¡ENCENDER MECHA!"):
    st.balloons()
    st.success("¡Senyor pirotècnic, pot començar la mascletà!")

st.header("🥨 En la Carpa")
tab1, tab2 = st.tabs(["🥘 Paella Pro", "🍩 Buñuelos Time"])
with tab1: st.image("https://imgcom.masterd.es/12/blog/2016/04/37226.jpg", width=400)
with tab2: st.image("https://bing.com/th?id=OSK.36b427fefce57fd7b3bce537f710fc63", width=400)

# --- SIDEBAR ---
st.sidebar.title("📍 Ubicación")
st.sidebar.write("Cruce C/ San Ramón con Av. de la Pólvora.")
st.sidebar.button("Hacerse Fallero")

st.markdown("---")
st.markdown("© 2026 Falla San Ramón - 'Sempre en peu, mai de genolls'")
