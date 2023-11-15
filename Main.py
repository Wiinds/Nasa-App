import requests
import streamlit as st 
import os

#Your current NASA API key 
api_key = os.getenv("NASA_API")


#NASA APOD API URL, with key 
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

# Get the request data as a Dict
response = requests.get(url)
data = response.json()

print(data)

#Extract the image title, url and explanation
data_title = data["title"]
image_url = data["url"]
date = data["date"]
explanation = data["explanation"]

# Download daily image 
image_filepath = "dailynasa_img.png"
response2 = requests.get(image_url)
with open(image_filepath, 'wb') as file:
    file.write(response2.content)
 
# title, daily photo and explaination 
st.title("Daily Nasa Photo")
st.subheader(data_title)

st.image(image_filepath)

st.subheader("Todays Info")
st.write(f"Current Date: {date}")
st.info(explanation)









