import streamlit as st

# Constante de los gases ideales en atm·L/mol·K
R = 0.0821

st.title("🌡️ Calculadora de la Ecuación de los Gases Ideales")
st.write("Resuelve PV = nRT. Selecciona la variable que deseas calcular:")

opcion = st.selectbox("Selecciona una variable a calcular", ["Presión (P)", "Volumen (V)", "Temperatura (T)", "Número de moles (n)"])

if opcion == "Presión (P)":
    V = st.number_input("Volumen (L)", min_value=0.01)
    n = st.number_input("Número de moles (mol)", min_value=0.01)
    T = st.number_input("Temperatura (K)", min_value=0.01)
    if st.button("Calcular Presión"):
        P = (n * R * T) / V
        st.success(f"Presión = {P:.3f} atm")

elif opcion == "Volumen (V)":
    P = st.number_input("Presión (atm)", min_value=0.01)
    n = st.number_input("Número de moles (mol)", min_value=0.01)
    T = st.number_input("Temperatura (K)", min_value=0.01)
    if st.button("Calcular Volumen"):
        V = (n * R * T) / P
        st.success(f"Volumen = {V:.3f} L")

elif opcion == "Temperatura (T)":
    P = st.number_input("Presión (atm)", min_value=0.01)
    V = st.number_input("Volumen (L)", min_value=0.01)
    n = st.number_input("Número de moles (mol)", min_value=0.01)
    if st.button("Calcular Temperatura"):
        T = (P * V) / (n * R)
        st.success(f"Temperatura = {T:.3f} K")

elif opcion == "Número de moles (n)":
    P = st.number_input("Presión (atm)", min_value=0.01)
    V = st.number_input("Volumen (L)", min_value=0.01)
    T = st.number_input("Temperatura (K)", min_value=0.01)
    if st.button("Calcular número de moles"):
        n = (P * V) / (R * T)
        st.success(f"n = {n:.3f} mol")
