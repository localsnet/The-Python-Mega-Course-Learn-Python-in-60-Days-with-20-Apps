import random
import requests
import streamlit as st

# Prepare API key and  API url
api_key = "o6IZ8D8mWubQFT3uVsIS7iJu9kHKj4cCt65uXmWA"
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}&date={random.randint(1996, 2022)}-{random.randint(1, 12)}-{random.randint(1, 30)}"

# Get thew request data as a dictionary
response1 = requests.get(url)
content = response1.json()
explanation = content.get("explanation")


# Using more reliable Download option:
image_filepath = "img.png"
response2 = requests.get(content.get("url"))
with open(image_filepath, 'wb') as file:
      file.write(response2.content)

st.title(content.get("title"))
st.image(image_filepath)
# Or short option:
#st.image(content.get("url"), width=600)


st.write(content.get("date"))
st.write(explanation)
