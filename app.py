import streamlit as st

# App Title
st.set_page_config(page_title="Simple Calculator", page_icon="🧮")
st.title("🧮 Simple Calculator")

# Input fields
num1 = st.number_input("Enter first number", value=0.0, step=1.0)
num2 = st.number_input("Enter second number", value=0.0, step=1.0)

# Operation selection
operation = st.selectbox("Choose an operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# Perform calculation
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    
    st.success(f"Result: {result}")
