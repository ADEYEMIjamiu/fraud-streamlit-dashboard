import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_csv("FraudShield_Banking_Data.csv")

df = load_data()

st.title("Risk Factors")

st.subheader("International Transactions")
intl = pd.crosstab(df["Is_International_Transaction"], df["Fraud_Label"])
st.bar_chart(intl)
st.write("This chart checks whether international transactions are more likely to be fraudulent. It helps the business evaluate cross-border transaction risk.")

st.subheader("Unusual Time Transactions")
unusual = pd.crosstab(df["Unusual_Time_Transaction"], df["Fraud_Label"])
st.bar_chart(unusual)
st.write("This chart shows whether transactions made at unusual times are linked with fraud. It supports fraud monitoring based on transaction timing.")

st.subheader("Previous Fraud Count")
prev = df.groupby("Fraud_Label")["Previous_Fraud_Count"].mean()
st.bar_chart(prev)
st.write("This chart examines whether customers with a prior fraud history are more associated with current fraud cases. It helps identify repeat-risk behaviour.")

st.subheader("Distance From Home")
distance = df.groupby("Fraud_Label")["Distance_From_Home"].mean()
st.bar_chart(distance)
st.write("This chart shows whether fraudulent transactions tend to happen farther from the customer’s normal location. It helps detect suspicious geographic behaviour.")