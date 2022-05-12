import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache
def load_data():
    df = pd.read_csv("esg.csv")
    return df
def load_data2():
    df1 = pd.read_csv("pdata.csv")
    return df1
df = load_data()
df1 = load_data2()

def show_explore_page():
    st.title("Анализ ESG рейтинга компаний")
    st.caption(
    """
    ##### Данные по 16 крупнейшим российским компаниям за 3 года (2019–2021 гг.) использовались в работе. ESG-оценки были собраны с RAEX-Europe. Информация о выручке компаний взяты с интернет-ресурса «smart-lab.ru», который представляет крупное в России сообщество инвесторов и трейдеров.
    """
    )
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader(
            """
            Средний ESG по компаниям
            """
            )
        data = df1.groupby(["Name"])["ESG"].mean().sort_values(ascending=True)
        st.bar_chart(data)
        st.subheader(
        """
        Cредняя выручка с учетом ESG индекса
        """
        )
        data = df1.groupby(["ESG"])["Annual_Profit"].mean().sort_values(ascending=True)
        st.line_chart(data, width=80)
    
    with col2:
       st.table(data=df1)
    
    
