import streamlit as st
import pandas as pd
import pickle

# Load the pre-trained machine learning model
ml = pickle.load(open('LinearRegressionModel.pkl','rb')) #LinearRegressionModel.pkl

# Define the app
def app():
    # Set the app title
    st.subheader(':blue[Welcome to,]')
    st.title('Second Hand Car Price Prediction')
    
    # Add some instructions
    st.write('Enter the details of the car to get an estimated price.')
    
    # Add input fields for car details
    # model = st.text_input('Model of car')
    model = st.selectbox('Model of car',('hyundai santro xing', 'mahindra jeep cl550', 'hyundai grand i10',
       'ford ecosport titanium', 'ford figo', 'hyundai eon',
       'ford ecosport ambiente', 'maruti suzuki alto',
       'skoda fabia classic', 'maruti suzuki stingray',
       'hyundai elite i20', 'mahindra scorpio sle', 'audi a8', 'audi q7',
       'mahindra scorpio s10', 'hyundai i20 sportz',
       'maruti suzuki vitara', 'mahindra bolero di',
       'maruti suzuki swift', 'maruti suzuki wagon', 'toyota innova 2.0',
       'renault lodgy 85', 'skoda yeti ambition', 'maruti suzuki baleno',
       'renault duster 110', 'renault duster 85', 'honda city 1.5',
       'maruti suzuki dzire', 'honda amaze', 'honda amaze 1.5',
       'honda city', 'datsun redi go', 'maruti suzuki sx4',
       'mitsubishi pajero sport', 'honda city zx', 'tata indigo ecs',
       'volkswagen polo highline', 'chevrolet spark ls',
       'renault duster 110ps', 'mini cooper s', 'skoda fabia 1.2l',
       'renault duster', 'mahindra scorpio s4', 'mahindra scorpio vlx',
       'mahindra quanto c8', 'ford ecosport', 'honda brio',
       'volkswagen vento highline', 'hyundai i20 magna',
       'toyota corolla altis', 'hyundai verna transform', 'bmw 3 series',
       'maruti suzuki a', 'toyota etios gd', 'ford figo diesel',
       'chevrolet beat lt', 'bmw 7 series', 'mahindra xuv500 w8',
       'hyundai i10 magna', 'hyundai verna fluidic',
       'maruti suzuki ertiga', 'honda amaze 1.2', 'hyundai i20 asta',
       'maruti suzuki eeco', 'maruti suzuki esteem', 'maruti suzuki ritz',
       'toyota etios liva', 'chevrolet spark', 'nissan micra xv',
       'chevrolet beat', 'ford ecosport trend', 'tata indica v2',
       'hindustan motors ambassador', 'toyota innova 2.5',
       'volkswagen jetta highline', 'volkswagen polo comfortline',
       'volkswagen polo', 'mahindra scorpio', 'nissan sunny',
       'renault kwid', 'chevrolet spark lt', 'fiat punto emotion',
       'hyundai i10 sportz', 'chevrolet beat ls', 'tata indigo cs',
       'hyundai eon era', 'mahindra xuv500', 'ford fiesta', 'hyundai i20',
       'hyundai fluidic verna', 'fiat petra elx', 'maruti suzuki ciaz',
       'maruti suzuki zen', 'hyundai creta 1.6', 'mahindra scorpio slx',
       'tata nano cx', 'tata sumo victa', 'volkswagen passat diesel',
       'renault scala rxl', 'hyundai i20 active', 'mahindra xylo e4',
       'mahindra jeep mm', 'mahindra bolero sle', 'force motors force',
       'toyota etios', 'honda city vx', 'mahindra thar crde',
       'audi a4 1.8', 'mercedes benz gla', 'land rover freelander',
       'renault kwid rxt', 'tata aria pleasure', 'mercedes benz b',
       'datsun go t', 'honda jazz vx', 'chevrolet tavera neo',
       'hyundai eon sportz', 'tata sumo gold', 'chevrolet enjoy 1.4',
       'nissan terrano xl', 'maruti suzuki maruti', 'renault kwid 1.0',
       'hyundai accent glx', 'mahindra tuv300 t4', 'honda accord',
       'mahindra scorpio 2.6', 'honda mobilio', 'skoda laura',
       'tata manza aura', 'chevrolet sail uva', 'audi a4 2.0',
       'hyundai elantra sx', 'mahindra kuv100 k8', 'hyundai i10',
       'hyundai accent', 'hyundai verna', 'toyota fortuner',
       'mahindra bolero power', 'skoda rapid elegance',
       'tata vista quadrajet', 'chevrolet beat diesel',
       'hyundai verna 1.4', 'maruti suzuki versa', 'tata indigo lx',
       'volkswagen vento konekt', 'mercedes benz c', 'maruti suzuki omni',
       'hyundai sonata transform', 'honda jazz s', 'mahindra scorpio w',
       'honda brio v', 'mahindra tuv300 t8', 'nissan x trail',
       'ford ikon 1.3', 'toyota fortuner 3.0', 'tata manza elan',
       'mercedes benz a', 'tata indigo ls', 'hyundai verna 1.6',
       'bmw 5 series', 'skoda superb 1.8', 'audi q3 2.0',
       'ford figo duratorq', 'mahindra logan diesel', 'tata nano genx',
       'honda city sv', 'ford figo petrol', 'toyota corolla h2',
       'hyundai xcent base', 'hyundai accent executive', 'tata zest xe',
       'mahindra xuv500 w6', 'tata tigor revotron', 'maruti suzuki 800',
       'honda mobilio s', 'tata indica', 'honda brio vx', 'tata nano lx',
       'jaguar xe xe', 'hyundai eon magna', 'hyundai eon d',
       'maruti suzuki estilo', 'mitsubishi lancer 1.8', 'ford fiesta sxi',
       'audi a6 2.0', 'hyundai getz prime', 'hyundai santro',
       'chevrolet beat ps', 'bmw x1 xdrive20d', 'tata nano',
       'chevrolet cruze ltz', 'mahindra xuv500 w10', 'hyundai accent gle',
       'force motors one', 'chevrolet spark 1.0', 'renault duster 85ps',
       'chevrolet enjoy', 'jeep wrangler unlimited', 'hyundai verna vgt',
       'maruti suzuki celerio', 'tata zest quadrajet', 'hyundai i10 era',
       'tata indigo marina', 'hyundai xcent sx', 'mahindra xylo e8',
       'tata manza aqua', 'tata venture ex', 'skoda octavia classic',
       'ford ikon 1.6', 'nissan sunny xl', 'volkswagen polo trendline',
       'hyundai elantra 1.8', 'tata indica ev2', 'jaguar xf 2.2',
       'audi q5 2.0', 'bmw x1 sdrive20d', 'maruti suzuki s',
       'volkswagen vento comfortline', 'mahindra kuv100',
       'volkswagen jetta comfortline', 'volvo s80 summum', 'bmw x1',
       'renault duster rxl', 'honda wr v', 'mahindra scorpio lx',
       'audi a3 cabriolet', 'hyundai santro ae', 'mahindra xylo d2',
       'hyundai getz gle', 'nissan micra xl', 'chevrolet tavera ls',
       'tata tiago revotron', 'tata tiago revotorq', 'ford fusion 1.4',
       'fiat linea emotion', 'toyota corolla', 'tata sumo grande',
       'volkswagen polo highline1.2l', 'hyundai creta', 'tata bolt xm',
       'datsun go plus', 'ford endeavor 4x4', 'mahindra logan',
       'chevrolet sail 1.2', 'tata manza', 'toyota etios g',
       'toyota qualis', 'mahindra quanto c4', 'hyundai i20 select',
       'hyundai getz', 'skoda fabia', 'tata zest xm'))
    # make = st.text_input('Company of car')
    make = st.selectbox('Comapny of car',('hyundai', 'mahindra', 'ford', 'maruti', 'skoda', 'audi', 'toyota',
       'renault', 'honda', 'datsun', 'mitsubishi', 'tata', 'volkswagen',
       'chevrolet', 'mini', 'bmw', 'nissan', 'hindustan', 'fiat', 'force',
       'mercedes', 'land', 'jaguar', 'jeep', 'volvo'))
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
        st.header("The predicted price of your car is: "+ "Rs." + str(int((ml.predict((input_data)))))+" /-")

    # # Make a prediction using the input data
    #  predicted_price = model.predict(input_data)[0]
    
    # # Display the predicted price
    # st.write('Estimated price: $', predicted_price)
    
# Run the app
# to run the app code: "streamlit run app.py" in terminal
if __name__ == '__main__':
    app()
