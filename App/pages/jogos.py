import streamlit as st
import pandas as pd
import numpy as np
import datetime
from datetime import date

st.title("Jogos do Dia")

dia = st.date_input(
      "Data de Análise",
      date.today())

def load_data_jogos():
  API_KEY = "cmsa0nii002b34dw4b8vfwqma"
  DIA = date.isoformat()
  url = f"https://futpythontrader.com.br/api/jogos-do-dia?date={DIA}&format=csv&api_key={API_KEY}"

  jogos_do_dia = pd.read_csv(url)
  # display(jogos_do_dia)
  return jogos_do_dia

df_jogos = load_data_jogos()

st.dataframe(df_jogos)
