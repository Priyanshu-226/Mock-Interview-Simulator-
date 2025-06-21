from gtts import gTTS
import os

def generate_intro_audio(name: str, role: str) -> str:
    text = f"Hi {name}, you are giving the interview for the {role} role. This is an in-office job, and you will be required to work from the office Monday to Friday. If you agree to all these terms and conditions, please start with your introduction."
    filename = f"static/{name}_{role}.mp3"
    tts = gTTS(text)
    tts.save(filename)
    return filename