import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_csv("FraudShield_Banking_Data.csv")

df = load_data()

st.title("Fraud Insights")

st.subheader("Fraud vs Normal Transactions")
st.bar_chart(df["Fraud_Label"].value_counts())
st.write("This chart compares the number of fraudulent and normal transactions. It helps identify how common fraud is within the transaction system.")

st.subheader("Average Transaction Amount")
avg_amount = df.groupby("Fraud_Label")["Transaction_Amount (in Million)"].mean()
st.bar_chart(avg_amount)
st.write("This chart shows whether fraudulent transactions tend to involve higher or lower amounts than normal ones. This can help the business focus monitoring on risky transaction sizes.")

st.subheader("Fraud by Transaction Type")
fraud_type = pd.crosstab(df["Transaction_Type"], df["Fraud_Label"])
st.bar_chart(fraud_type)
st.write("This chart shows which transaction types are more associated with fraud. It helps the business identify channels that may need stronger controls.")