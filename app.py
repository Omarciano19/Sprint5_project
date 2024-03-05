import plotly.express as px
import streamlit as st
import pandas as pd

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.button('Construir histograma')  # crear un botón
disp_button = st.button('Construir grafico de dispersión')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

# mostrar un gráfico Plotly interactivo
st.plotly_chart(fig, use_container_width=True)

if disp_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un grafico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.scatter(car_data, y="price", x="odometer")

# mostrar un gráfico Plotly interactivo
st.plotly_chart(fig, use_container_width=True)