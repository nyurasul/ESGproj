import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

page = st.selectbox("Выберите страницу для просмотра", ("Спрогнозировать ESG индекс", "Изучить данные по модели"))

if page == "Спрогнозировать ESG индекс":
    show_predict_page()
else:
    show_explore_page()