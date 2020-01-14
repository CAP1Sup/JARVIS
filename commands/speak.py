import os

def speak(audio):
    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)