# Import libraries
import speech_recognition as sr
import os
import sys
import re
import webbrowser
import requests
import subprocess
from pyowm import OWM
import smtplib
import youtube_dl
import urllib
import json
from bs4 import BeautifulSoup as soup
import wikipedia
import random
from time import strftime

# Import custom commands
from commands.contact_info import *
#from commands.speak import *


def main():
    while True:
        JARVIS(get_words())


def get_words():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('....')
        command = get_words()
    return command


def separate_commands(command):
    commands = []
    last_found_and_start = 0

    while True:
        and_location = command.find('and', last_found_and_start)
        if and_location == -1:
            # No ands found
            commands.append(command)
            break

        elif command.find('and', and_location + 1) != -1:
            # See it there is another 'and' in the command, and cut that portion out if there is
            next_and_location = command.find('and', and_location + 1)
            commands.append( command[ and_location:next_and_location ] )
        else:
            # Only a single and command found
            pass


            

def JARVIS(command):
    # If statements for commands
    
    if 'repeat ' in command:
        pass

    elif 'open ' in command:
        pass

main()