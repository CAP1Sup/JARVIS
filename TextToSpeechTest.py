from gtts import gTTS
import os
import playsound
from google.cloud import texttospeech

global i

def speakText(text):
    tts = gTTS(text=text, lang="en")
    tts.save(i + ".mp3")
    playsound.playsound(i + '.mp3', True)


def speakTextLang(text, lang):
    tts = gTTS(text=text, lang=lang)
    tts.save("voice.mp3")
    playsound.playsound('voice.mp3', True)

i = 1
speakText( text = "Hi!")
speakText( text= "How are you today?")