import sys
import streamlit as st
import pickle
import numpy as np
import pandas as pd

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]

def show_predict_page():
    st.title("Прогнозирование вашего ESG индекса")
    st.caption(
        """
    ###### ESG (Environmental, Social and Governance) рейтинг представляет собой экспертное мнение Агентства, выраженное символьным (буквенным) показателем, в отношении подверженности компании экологическим и социальным рискам бизнеса, а также рискам корпоративного управления, на основе оценки качества соблюдения соответствующих практик и их соответствия базовым международным и российским ориентирам, стандартам и лучшим практикам в области устойчивого развития.
    """
    )
    st.image("https://raex-a.ru/files/files/esg130421.png")
    
    st.sidebar.write("""### Нам нужна некоторая информация, чтобы сделать прогноз""")

    e = st.sidebar.slider("E оценка", 0, 200, 3)
    s = st.sidebar.slider("S оценка", 0, 200, 3)
    g = st.sidebar.slider("G оценка", 0, 200, 3)
    ap = st.sidebar.number_input("Годовая выручка (млн руб)", 0)
   

    ok = st.sidebar.button("Рассчитать ESG индекс")
    if ok:
        X = np.array([[e, s, g, ap]])
        X = X.astype(float)
        esg = regressor.predict(X)
        st.sidebar.subheader(f" Предположительное значение ESG индекса = {esg[0]:.0f}")
