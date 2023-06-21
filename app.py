import streamlit as st
import pandas as pd
import pickle

# Load the pre-trained machine learning model
ml = pickle.load(open('LinearRegressionModel.pkl','rb')) #LinearRegressionModel.pkl

# Define the app
def app():
    # Set the app title
    st.subheader(':blue[Welcome to,]')
    st.title(' Second Hand Car Price Prediction')
    
    # Add some instructions
    st.write('Enter the details of the car to get an estimated price.')
    
    # Add input fields for car details
    model = st.text_input('Model of car')
    make = st.text_input('Company of car')
    # year = st.number_input('Year of manufacture',  step=1)
    year = st.slider('Select a year of manufacture',2003,2023)
    mileage = st.number_input('Distance covered (in kms)',value=20000,step=1000)
    fuel = st.selectbox('fuel', ('Petrol', 'Diesel', 'LPG'))
    
    #lower casing the inputs
    model=model.lower()
    make=make.lower()
    
    # Create a pandas dataframe with the input values    #'name','company','year','kms_driven','fuel_type'
    input_data = pd.DataFrame({
        'name': model,
        'company': make,
        'year': year,
        'kms_driven': mileage,
        'fuel_type': fuel
    }, index=[0])
    if st.button("submit") :
        st.header("The predicted price of your car is : " + str(int((ml.predict((input_data)))))+ " Rs")

    # # Make a prediction using the input data
    #  predicted_price = model.predict(input_data)[0]
    
    # # Display the predicted price
    # st.write('Estimated price: $', predicted_price)
    
# Run the app
# to run the app code: "streamlit run app.py" in terminal
if __name__ == '__main__':
    app()
