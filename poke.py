# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import json
import webbrowser
import speech_recognition as sr


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
try:
    name = r.recognize_google(audio)
    name = name.lower()
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio") 
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

print (name)

def getpokeimage(text):
    #pok = raw_input("Name :")
    try:
        url = 'https://pokeapi.co/api/v2/pokemon/'+ text
        resp = requests.get(url)
        data = json.loads(resp.content.decode())
    except requests.HTTPError as e:
        code  = e.response.status_code
        raise("The response from the API is :",code)
    
    num = str(data.get("id"))
    img = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/"+ num +".png"
    webbrowser.open(img)


getpokeimage(name) 
