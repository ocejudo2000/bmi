import streamlit as st

st.title('BMI Calculator')

weight = st.number_input('Enter your weight (in kg)', min_value=0.0, format='%f')
height = st.number_input('Enter your height (in meters)', min_value=0.0, format='%f')

if weight > 0 and height > 0:
    bmi = weight / (height ** 2)
    st.write(f'Your BMI is: {bmi:.2f}')
    if bmi < 18.5:
        st.write("You're in the underweight range.")
    elif bmi < 25:
        st.write("You're in the healthy weight range.")
    elif bmi < 30:
        st.write("You're in the overweight range.")
    else:
        st.write("You're in the obese range.")