import streamlit as st

# Función principal de conversión
def convertir_temperatura(valor, unidad_origen, unidad_destino):
    # Si las unidades son iguales, retornamos el mismo valor
    if unidad_origen == unidad_destino:
        return valor
    
    # Para simplificar, primero convertimos la unidad de origen a Celsius
    if unidad_origen == "Fahrenheit":
        celsius = (valor - 32) * 5.0 / 9.0
    elif unidad_origen == "Kelvin":
        celsius = valor - 273.15
    else: # Si ya es Celsius
        celsius = valor

    # Luego, convertimos de Celsius a la unidad de destino solicitada
    if unidad_destino == "Fahrenheit":
        resultado = (celsius * 9.0 / 5.0) + 32.0
    elif unidad_destino == "Kelvin":
        resultado = celsius + 273.15
    else: # Si el destino es Celsius
        resultado = celsius
        
    return resultado

# Configuración de la página
st.set_page_config(page_title="Conversor de Temperatura", page_icon="🌡️", layout="centered")

# Título y descripción de la aplicación
st.title("🌡️ Conversor de Temperatura")
st.markdown("Convierte fácilmente valores entre grados **Celsius**, **Fahrenheit** y **Kelvin**.")
st.divider()

# Creación de columnas para organizar la interfaz
col1, col2 = st.columns(2)

unidades = ["Celsius", "Fahrenheit", "Kelvin"]

# Controles de entrada en la primera columna
with col1:
    valor_ingresado = st.number_input("Valor a convertir:", value=0.0, format="%.2f")
    unidad_origen = st.selectbox("Unidad de origen:", unidades, index=0)

# Controles de entrada en la segunda columna
with col2:
    unidad_destino = st.selectbox("Unidad de destino:", unidades, index=1)

# Cálculo y visualización del resultado
resultado = convertir_temperatura(valor_ingresado, unidad_origen, unidad_destino)

st.divider()

# Mostrar el resultado final de forma destacada
st.success(f"### {valor_ingresado:.2f} {unidad_origen} equivale a {resultado:.2f} {unidad_destino}")

# Nota adicional sobre el cero absoluto
if unidad_origen == "Kelvin" and valor_ingresado < 0:
    st.warning("Nota: El cero absoluto es 0 Kelvin. Los valores negativos en la escala Kelvin no existen en la física clásica.")
elif unidad_origen == "Celsius" and valor_ingresado < -273.15:
    st.warning("Nota: La temperatura ingresada es inferior al cero absoluto (-273.15 °C).")
elif unidad_origen == "Fahrenheit" and valor_ingresado < -459.67:
    st.warning("Nota: La temperatura ingresada es inferior al cero absoluto (-459.67 °F).")