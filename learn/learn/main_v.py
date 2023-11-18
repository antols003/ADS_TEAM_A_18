import streamlit as st
import openai
import speech_recognition as sr
import pyttsx3
from PIL import Image
import time
from moviepy.editor import * 

# Set your API key here
api_key = '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'
openai.api_key = api_key

# Function to interact with the chatbot
def chat_with_openai(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Function for voice recognition
# Function for voice recognition
def recognize_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    
    with mic as source:
        st.write("Speak:")
        try:
            audio = recognizer.listen(source)
            user_input = recognizer.recognize_google(audio)
            return user_input
        except sr.UnknownValueError:
            st.write("Sorry, I couldn't understand the audio.")
            return ""
        except sr.RequestError:
            st.write("Sorry, there was an error with the speech recognition service.")
            return ""


# Function for text-to-speech
def speak_text(text):
    engine = pyttsx3.init()
    engine.save_to_file(text, 'output.mp3')
    engine.runAndWait()

# Function to create a video from the audio response
def generate_video_response(text_response):
    speak_text(text_response)
    audio = AudioFileClip("output.mp3")
    video = ImageClip("C:\\Users\\student.MCC\\Downloads\\learn\\learn\\path_to_avatar_1.jpg").set_duration(audio.duration)
    video = video.set_audio(audio)
    video.write_videofile("output.mp4", codec='libx264', fps=24)

# Main function to start a conversation with the chatbot
def main():
    st.title("Learn Buddy")

    st.write("Welcome to the Learn Buddy! Speak or type 'exit' to end the conversation.")
    
    input_method = st.radio("Select input method:", ("Voice", "Text"))

    if input_method == "Voice":
        user_input = recognize_speech()
    else:
        user_input = st.text_input("You:")

    if st.button("Send"):
        if user_input.lower() == 'exit':
            st.write("Conversation ended.")
        else:
            chatbot_response = chat_with_openai(user_input)
            st.write("Learn Buddy:", chatbot_response)
            generate_video_response(chatbot_response)
            st.video("output.mp4")

from moviepy.editor import *
import subprocess

# Function to combine audio and video
def create_video_from_audio(audio_file, video_file, output_file):
    audio = AudioFileClip(audio_file)
    video = VideoFileClip(video_file).subclip(0, audio.duration)
    final_video = video.set_audio(audio)
    final_video.write_videofile(output_file, codec='libx264', fps=24)

# Function to display the generated video
def display_video(video_file):
    video = VideoFileClip(video_file)
    video.ipython_display(width=480)

# Assuming you have a video of a person talking named 'human_video.mp4' and an audio file 'output.mp3'
audio_file = "C:\\Users\\student.MCC\\Downloads\\learn\\learn\\output.mp3"
video_file = "C:\\Users\\student.MCC\\Downloads\\learn\\learn\\human_video.mp4"
output_file = "C:\\Users\\student.MCC\\Downloads\\learn\\learn\\output_video.mp4"
def display_video(output_file):
    st.video(output_file)

create_video_from_audio(audio_file, video_file, output_file)
display_video(output_file)

            
if __name__ == "__main__":
    main()
