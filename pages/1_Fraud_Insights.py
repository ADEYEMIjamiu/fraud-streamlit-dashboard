import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_csv("FraudShield_Banking_Data.csv")

df = load_data()

st.title("Fraud Insights")

# --- Fraud vs Normal ---
st.subheader("Fraud vs Normal Transactions")
st.bar_chart(df["Fraud_Label"].value_counts())
st.write("This chart compares fraudulent and normal transactions, helping to understand how common fraud is within the system.")

# --- Average Amount ---
st.subheader("Average Transaction Amount")
avg_amount = df.groupby("Fraud_Label")["Transaction_Amount (in Million)"].mean()
st.bar_chart(avg_amount)
st.write("Fraudulent transactions often involve higher amounts, indicating that fraudsters target high-value opportunities.")

# --- Transaction Type ---
st.subheader("Fraud by Transaction Type")
fraud_type = pd.crosstab(df["Transaction_Type"], df["Fraud_Label"])
st.bar_chart(fraud_type)
st.write("Online transactions show higher fraud activity, suggesting increased risk in digital payment channels.")

st.subheader("Fraud vs Normal Trend Over Time")

# Convert to datetime
df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"])

# Create trend data
trend_data = (
    df.groupby(["Transaction_Date", "Fraud_Label"])
    .size()
    .unstack(fill_value=0)
)

# Plot line chart
st.line_chart(trend_data)

# Insight text
st.write("This line chart shows how fraud and normal transactions change over time. It helps identify patterns or spikes in fraudulent activity across different periods.")
