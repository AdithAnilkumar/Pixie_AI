import pygame  # Import pygame library for handling audio playback
import random  # Import random for generating random choices
import asyncio # Import asyncio for asynchronous operations
import edge_tts # Import edge_tts for text-to-speech functionality
import os      # Import os for file path handling
from pathlib import Path
from dotenv import dotenv_values # Import dotenv for reading environment variables

# Resolve project paths relative to this file.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
SPEECH_PATH = PROJECT_ROOT / "Data" / "speech.mp3"

# Load environment variables from a .env file
env_vars = dotenv_values(".env")
AssistantVoice = env_vars.get("AssistantVoice") or env_vars.get("ASSISTANT_VOICE") or "en-US-AriaNeural" # Get the AssistantVoice from environment variables

import re

def clean_text_for_speech(raw_text: str) -> str:
    """Strip markdown headers, asterisks, hash symbols, and code blocks for clean spoken audio."""
    text = str(raw_text or "")
    # Remove code blocks
    text = re.sub(r"```[\s\S]*?```", " Code block output is shown on screen. ", text)
    # Remove headers ###, ##, #
    text = re.sub(r"#{1,6}\s*", "", text)
    # Remove bold / italic asterisks and underscores
    text = re.sub(r"[*_]{1,3}", "", text)
    # Clean bullet dash lists
    text = re.sub(r"^\s*[-*+]\s+", "", text, flags=re.MULTILINE)
    # Remove backticks
    text = re.sub(r"`", "", text)
    return text.strip()

# Asynchronous function to convert text to an audio file
async def TextToAudioFile(text) -> None:
    file_path = SPEECH_PATH # Define the path where the speech file will be saved
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    if file_path.exists(): # Check if the file already exists
        file_path.unlink()     # If it exists, remove it to avoid overwriting errors
        
    cleaned_speech_text = clean_text_for_speech(text)
    if not cleaned_speech_text:
        cleaned_speech_text = "Done."

    # Create the communicate object to generate speech
    communicate = edge_tts.Communicate(cleaned_speech_text, AssistantVoice, pitch='+5Hz', rate='+13%')
    await communicate.save(str(file_path)) # Save the generated speech as an MP3 file

# Function to manage Text-to-Speech (TTS) functionality
def TTS(Text, func=lambda r=None: True):
    while True:
        try:
            # Convert text to an audio file asynchronously
            asyncio.run(TextToAudioFile(Text))
            
            # Initialize pygame mixer for audio playback
            pygame.mixer.init()
            
            # Load the generated speech file into pygame mixer
            pygame.mixer.music.load(str(SPEECH_PATH))
            pygame.mixer.music.play() # Play the audio
            
            # Loop until the audio is done playing
            while pygame.mixer.music.get_busy():
                if func() == False: # Check if the external function returns False
                    break
                pygame.time.Clock().tick(10) # Limit the loop to 10 ticks per second
                
            return True # Return True if the audio played successfully
            
        except Exception as e: # Handle any exceptions during the process
            print(f"Error in TTS: {e}")
            
        finally:
            try:
                # Call the provided function with False to signal the end of TTS
                func(False)
                if pygame.mixer.get_init():
                    pygame.mixer.music.stop() # Stop the audio playback
                    pygame.mixer.quit()       # Quit the pygame mixer
                
            except Exception as e: # Handle any exceptions during cleanup
                print(f"Error in finally block: {e}")
            break

# Function to manage Text-to-Speech with additional responses for long text
def TextToSpeech(Text, func=lambda r=None: True):
    """Speak the full response text cleanly without truncating."""
    TTS(Text, func)

# Main execution loop
if __name__ == "__main__":
    while True:
        # Prompt user for input and pass it to the TTS function
        user_input = input("Enter text to speak: ")
        if user_input.lower() == "exit":
            break
        TextToSpeech(user_input)
