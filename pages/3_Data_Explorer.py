import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_csv("FraudShield_Banking_Data.csv")

df = load_data()

st.title("Data Explorer")

# Clean dropdown values
label_options = ["All"] + sorted(df["Fraud_Label"].dropna().astype(str).unique().tolist())
txn_options = ["All"] + sorted(df["Transaction_Type"].dropna().astype(str).unique().tolist())

label = st.sidebar.selectbox("Fraud Label", label_options)
txn = st.sidebar.selectbox("Transaction Type", txn_options)

if label != "All":
    df = df[df["Fraud_Label"].astype(str) == label]

if txn != "All":
    df = df[df["Transaction_Type"].astype(str) == txn]

st.subheader("Filtered Data")
st.dataframe(df)