import streamlit as st
import pandas as pd
import joblib

st.title("You can know the weight!")

st.image("fish_market.jpg", width = 700)

st.text("Please, if you want a correct answer, introduce a real data.")

specie = st.selectbox("Select Specie", ('Bream', 'Roach', 'Whitefish', 'Parkki', 'Pike', 'Perch', 'Smelt'))
col1, col2  = st.columns(2)
with col1:
    height = st.number_input("Enter Height in cm", min_value=0.00)
with col2:
    width = st.number_input("Enter Width in cm", min_value=0.00)
col1, col2, col3 = st.columns(3)
with col1:
    length_vertical = st.number_input("Enter Length Vertical in cm", min_value=0.00)
with col2:
    length_diagonal = st.number_input("Enter Length Diagonal in cm", min_value=0.00)
with col3:
    length_cross = st.number_input("Enter Length Cross in cm", min_value=0.00)

if st.button('Submit'):
    if height == 0 or width == 0 or length_vertical == 0 or length_cross == 0 or length_diagonal == 0:
        st.text("Debe rellenar todos los campos")
    else:
        # Unpickle classifier
        pet_model = joblib.load("fish_market_model.pkl")

        # Store inputs into dataframe
        X = pd.DataFrame([
            [specie, length_vertical, length_diagonal, length_cross, height, width]],
            columns = ["Species", "LengthVertical", "LengthDiagonal", "LengthCross", "Height", "Width"])
        X = X.replace(
            ['Bream', 'Roach', 'Whitefish', 'Parkki', 'Pike', 'Perch', 'Smelt'],
            [1,2,3,4,5,6,7])

        # Get prediction
        prediction = pet_model.predict(X)[0]

        st.write(f"The fish's weight is around {prediction} gr")
