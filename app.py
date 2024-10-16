import streamlit as st
import pickle
import mysql.connector as connector
connection=connector.connect(user="admin1",password="123456")
cursor=connection.cursor()
use_db='''USE mg_schema'''
cursor.execute(use_db)
st.title("Mobile Price Predictor")

 

status=st.radio("Select an option: ",("Predict","Enter data"))
if status=="Predict":
    Ratings=st.number_input("Enter Rating")
    RAM=st.number_input("Enter RAM")
    ROM=st.number_input("Enter ROM")
    Mobile_size=st.number_input("Enter Size")
    Primary_cam=st.number_input("Enter Primary camera")
    Selfie_cam=st.number_input("Enter Selfie camera")
    Battery_Power=st.number_input("Enter Battery Power")
    rfr=pickle.load(open("model.pkl","rb"))
    st.write("Price: ",rfr.predict([[RAM,ROM,Mobile_size,Primary_cam,Selfie_cam,Battery_Power]]))
else:
    Ratings=st.number_input("Enter Rating")
    RAM=st.number_input("Enter RAM")
    ROM=st.number_input("Enter ROM")
    Mobile_size=st.number_input("Enter Size")
    Primary_cam=st.number_input("Enter Primary camera")
    Selfie_cam=st.number_input("Enter Selfie camera")
    Battery_Power=st.number_input("Enter Battery Power")
    Price=st.number_input("Enter Price")
    if st.button("Submit:"):
        val=(Ratings,RAM,ROM,Mobile_size,Primary_cam,Selfie_cam,Battery_Power,Price)
        insert_query='''INSERT INTO mobile_price VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'''
        cursor.execute(insert_query,val)
        connection.commit()

