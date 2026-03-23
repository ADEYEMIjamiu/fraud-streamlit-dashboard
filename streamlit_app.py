import streamlit as st
import pandas as pd

st.set_page_config(page_title="Fraud Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("FraudShield_Banking_Data.csv")

df = load_data()

# Sidebar filter
st.sidebar.header("Global Filter")

label_filter = st.sidebar.selectbox(
    "Fraud Label",
    ["All"] + sorted(df["Fraud_Label"].dropna().astype(str).unique().tolist())
)

if label_filter != "All":
    df = df[df["Fraud_Label"].astype(str) == label_filter]

st.title("Fraud Detection Dashboard")
st.write("This dashboard explores fraud patterns in banking transactions and highlights key risk indicators for business decision-making.")

col1, col2, col3 = st.columns(3)
col1.metric("Total Transactions", len(df))
col2.metric("Fraud Cases", (df["Fraud_Label"] == "Fraud").sum())
col3.metric("Average Amount (M)", f"{df['Transaction_Amount (in Million)'].mean():.2f}")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Fraud Distribution")
st.bar_chart(df["Fraud_Label"].value_counts())

fraud_rate = (df["Fraud_Label"] == "Fraud").mean() * 100
st.write(f"Fraud rate is approximately {fraud_rate:.2f}% of total transactions, indicating the proportion of suspicious activities within the dataset.")

st.write("This chart gives a quick overview of the balance between normal and fraudulent transactions in the dataset. It helps the business understand the scale of fraud relative to total activity.")