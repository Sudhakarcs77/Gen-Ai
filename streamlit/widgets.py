import streamlit as st
import pandas as pd

# streamlit.io docs 

st.title("Streamlit Text input")
name = st.text_input("Enter your name: ")

age = st.slider("Select your age: ", 0,100,25)
st.write(f"Your age is {age}")


options = ["Python", "C++", "JAVA","JavaScript" ]
choice = st.selectbox("Chioose your favorite language: ", options)
st.write(f"Your selected language {choice}")


if name:
    st.write(f"Hello {name}")


df = pd.DataFrame({
    "name": ["ram","sid","Ben","Krish","Raj"],
    "age": [10,20,30,40,50]
    })
#st.write(df)

df.to_csv("sample.csv")


upload = st.file_uploader("Choose a CSV file ", type="csv")

if upload:
    df = pd.read_csv(upload)
    st.write(df)


