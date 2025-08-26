import streamlit as st
import numpy as np

st.title("Contact Form")

# Collect user details
name = st.text_input("What is your name?")
email = st.text_input("Email")
audio = st.file_uploader("Upload an audio file", type=["mp3", "wav"])
message = st.text_area("Message", placeholder="Tell us about yourself")

# Camera input
camera = st.camera_input("Take a photo")

# Submit button
if st.button("Submit"):
    st.subheader("Submitted Information")

    if name:
        st.write("**Name:**", name)
    if email:
        st.write("**Email:**", email)
    if message:
        st.write("**Message:**", message)
    if audio:
        st.audio(audio)
    if camera:
        st.image(camera)

    # Example chat output after submit
    with st.chat_message("user"):
        st.write(f"My name is {name} and I just submitted the form.")

    with st.chat_message("assistant"):
        st.write("Thanks for submitting your details! 🎉")

