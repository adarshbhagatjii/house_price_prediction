import joblib 
import pandas as pd 
import streamlit as st  


st.set_page_config(page_title="House Price Prediction", page_icon="🏠", layout="wide")

with open('rf_model.joblib', 'rb') as file:
    model = joblib.load(file)

df=pd.read_csv('cleaned_df.csv')
st.title("House Price Prediction App")

with st.sidebar:
    st.title('house price prediction')
    st.image('houseimage.jpg', width=300)

def encoded_loc(location):
    for loc,encoded in zip(df['location'], df['encoded_location']):
        if loc == location:
            return encoded
        
with st.container(border=True):
    st.header("Enter the details of the house:")
    col1, col2 = st.columns(2)
    
    with col1:
        location = st.selectbox("Location", df['location'].unique())
        sqft = st.number_input("Square Footage", min_value=300, step=10)
        
    with col2:
        bhk = st.selectbox("BHK", options=df['bhk'].unique())

        bath = st.selectbox("Bathrooms", options=sorted(df['bath'].unique()))

    encoded_location = encoded_loc(location)


c1,c2,c3 = st.columns(3)
if c2.button("Predict Price"):
        inp_data=[[sqft,bhk,bath,encoded_location]]
        pred=model.predict(inp_data)
        pred=float(f'{pred[0]:.2f}')
        st.success(f"The predicted price of the house is: ₹{pred*100000}")

