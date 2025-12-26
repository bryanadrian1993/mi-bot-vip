import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# 1. Configuración de Estilo CSS para que se vea IGUAL
st.markdown("""
    <style>
    .stApp { background-color: white; }
    h1 { color: #FF4B4B; font-family: 'Arial'; font-weight: bold; text-align: center; }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        font-weight: bold;
    }
    /* Botón Registrar (Rojo) */
    div.stButton > button:first-child { background-color: #FF4B4B; color: white; border: none; }
    
    /* Botón PayPal (Azul) */
    .paypal-btn { background-color: #003087; color: white; padding: 10px; border-radius: 5px; 
                  text-align: center; display: block; text-decoration: none; font-weight: bold; }
                  
    /* Botón WhatsApp (Verde) */
    .wa-btn { background-color: #25D366; color: white; padding: 10px; border-radius: 5px; 
               text-align: center; display: block; text-decoration: none; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. Encabezado con Logo
st.markdown("<h1>🔥 ACTIVACIÓN VIP</h1>", unsafe_allow_html=True)

# 3. Paso 1: Registro
st.write("**1. Introduce tu WhatsApp:**")
numero = st.text_input("Ejemplo: +593999999999", value="+", label_visibility="collapsed")

if st.button("REGISTRAR NÚMERO"):
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("credenciales.json", scope)
        client = gspread.authorize(creds)
        hoja = client.open("Base_Datos_Bot").sheet1
        hoja.append_row([numero, "PENDIENTE", "PENDIENTE", 0])
        st.success(f"✅ ¡Número {numero} registrado correctamente!")
    except:
        st.error("❌ Error de conexión.")

st.markdown("<br>", unsafe_allow_html=True)

# 4. Paso 2: Pagos
st.write("**2. Elige tu método de pago:**")

# Botón PayPal estilizado
st.markdown('<a href="https://paypal.me/tu_usuario" class="paypal-btn">🔵 PAGAR $20 CON PAYPAL</a>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Botón Pichincha con lógica de QR
if st.button("🟡 PICHINCHA / DEUNA"):
    st.image("qr_pago.png", caption="Escanea para pagar")

st.markdown("<br>", unsafe_allow_html=True)

# 5. Paso 3: Comprobante
st.write("**3. ¿Ya pagaste? Envía el capture:**")
st.markdown(f'<a href="https://wa.me/tu_numero?text=Ya_pague_mi_suscripcion" class="wa-btn">✅ ENVIAR COMPROBANTE AL WHATSAPP</a>', unsafe_allow_html=True)
