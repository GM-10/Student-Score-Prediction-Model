import pickle
import streamlit as st

with open("performanceidx.pkl", mode="rb") as f:
    model1 = pickle.load(f)

def f1():
    st.title("STUDENT SCORE PREDICTION MODEL")

    hrsstudied = st.number_input("Enter the hours studied:")
    prescore = st.number_input("Enter Previous Scores:")
    exact = st.selectbox("Enter 1 for yes, 0 for no:", [0, 1])
    sleephrs = st.number_input("Enter the no. of hours slept:")
    qpp = st.number_input("Enter the no. of papers:")

    if st.button("Predict"):
        try:
            # Assuming model1 is a scikit-learn model
            performindx = model1.predict([[hrsstudied, prescore, exact, sleephrs, qpp]])[0] 
            st.success(f"Performance Index is: {performindx}")
        except Exception as e:
            st.error(f"Prediction failed: {e}")

f1()