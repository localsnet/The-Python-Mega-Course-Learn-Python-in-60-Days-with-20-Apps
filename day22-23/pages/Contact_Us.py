import streamlit as st
import pandas
from send_email import send_email


df = pandas.read_csv("topics.csv")

st.header("Contact me")

with st.form(key="email_forms"):
    topic = st.selectbox(
        "What topic do you want to discuss?",
        df
    )
    user_email = st.text_input("Your e-mail address")
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New e-mail from {user_email}

From: {user_email}
Topic: {topic}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    print(topic)
    if button:
        send_email(message)
        st.info("Your e-mail was send successfully")