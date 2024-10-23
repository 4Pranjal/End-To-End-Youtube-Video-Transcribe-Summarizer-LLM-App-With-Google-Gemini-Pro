import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

# Load environment variables from .env file
load_dotenv()

# Configure Google Generative AI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Prompt template for summarizing YouTube video transcripts
prompt = """
You are a YouTube video summarizer. You will take the transcript text 
and summarize the entire video, providing the important points in 250 words or less. 
Please provide the summary of the text given here: 
"""

# Function to extract transcript data from a YouTube video
def extract_transcript_details(youtube_video_url):
    try:
        # Extract video ID from the YouTube URL
        video_id = youtube_video_url.split("=")[1]
        
        # Retrieve the transcript using YouTubeTranscriptApi
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Concatenate the transcript text
        transcript = " ".join([i["text"] for i in transcript_text])
        return transcript

    except Exception as e:
        # Handle exceptions such as transcript not found
        raise e

# Function to generate summary based on the transcript and prompt
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    
    # Generate response from the model using the transcript and prompt
    response = model.generate_content(prompt + transcript_text)
    return response.text

# Streamlit app setup
st.title("YouTube Transcript to Detailed Notes Converter")

# Input field for YouTube video link
youtube_link = st.text_input("Enter YouTube Video Link:")

# Display the YouTube thumbnail if a valid link is provided
if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

# Button to fetch the transcript and generate the summary
if st.button("Get Detailed Notes"):
    # Extract the transcript from the provided YouTube video link
    transcript_text = extract_transcript_details(youtube_link)
    
    # Generate and display the summary if the transcript is successfully retrieved
    if transcript_text:
        summary = generate_gemini_content(transcript_text, prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)
