import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("pipedata.csv")


st.title("Pipe Data Lookup")

# Let user choose from available Nominal Dia and columns
nominal_dia = st.selectbox("Select Nominal Diameter (in inch)", df["Nominal Dia"].astype(str).unique())
column = st.selectbox("Select Pipe Schedule", df.columns[1:])

# Convert Nominal Dia to float to match dataframe type
try:
    nominal_dia = float(nominal_dia)
    result_row = df[df["Nominal Dia"] == nominal_dia]

    if not result_row.empty:
        value = result_row.iloc[0][column]
        if value == 0.0:
            st.write("Not Available")
        else:
            st.success(f'Internal Diameter for NB : "{nominal_dia}" and SCH : "{column}" is {value}')
            st.write("ID : ", value)
    else:
        st.error("No matching row found.")
except ValueError:
    st.error("Invalid Nominal Dia input.")
