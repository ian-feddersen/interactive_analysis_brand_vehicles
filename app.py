
import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos del archivo CSV
car_data = pd.read_csv("./data/vehicles_us.csv")

# Crear un encabezado
st.header('Análisis de Datos de Vehículos Usados en EE.UU.')


build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_histogram:
    st.write('Creación de un histograma para la columna odometer')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    st.write('Creación de un gráfico de dispersión para las columnas odometer y price')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)


