import streamlit as st
import pandas as pd



st.sidebar.header("Options")
text = st.sidebar.text_area("Paste Text Here")
st.write(text)

st.title("My First App!")
button1 = st.button("Click Me")
 
st.header("Checkbox Section")   
like = st.checkbox("Do you like this app?")
button2 = st.button("Submit") #checks if like is selected
if button2:
    st.write("Thanks.")
else:
    st.write("You have bad taste!")
 
st.header("Radio Section")   
color = st.radio("What is your favorite color?", ("Pink", "Yellow", "Blue", "Red", "Orange", 'Purple', 'Green', 'White', 'Black', 'Gray'))
button3 = st.button("Submit Color")
if button3:
    st.write(color)
        
st.header("Selectbox")   
color2 = st.selectbox("What is your favorite color?", ("Pink", "Yellow", "Blue", "Red", "Orange", 'Purple', 'Green', 'White', 'Black', 'Gray'))
button4 = st.button("Submit Color 2")
if button4:
    st.write(color2)
        
st.header("Multiselect")
options = st.multiselect("What is your favorite color?", ("Pink", "Yellow", "Blue", "Red", "Orange", 'Purple', 'Green', 'White', 'Black', 'Gray'))
button5 = st.button("Print Colors")
if button5:
    st.write(options)

user_num = st.number_input("What's your favorite number?")
if st.button("Number Button"):
    st.write(user_num)