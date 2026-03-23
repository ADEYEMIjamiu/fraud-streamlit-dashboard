import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="Fraud Dashboard", layout="wide")

## Load data
@st.cache_data
def load_data():
    return pd.read_csv("FraudShield_Banking_Data.csv")

df = load_data()

### Title
st.title("Fraud Detection Dashboard")

#### KPIs
col1, col2, col3 = st.columns(3)

col1.metric("Total Transactions", len(df))
col2.metric("Fraud Cases", (df["Fraud_Label"] == "Fraud").sum())
col3.metric("Average Amount", round(df["Transaction_Amount (in Million)"].mean(), 2))

##### Data preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

##### Chart
st.subheader("Fraud Distribution")
st.bar_chart(df["Fraud_Label"].value_counts())
