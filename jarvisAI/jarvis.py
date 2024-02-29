import speech_recognition as sr
import os
# import win32com.cliere
import webbrowser
import openai
import datetime
from config import apikey
import random
import wikipedia
import pyttsx3
import json

chatStr = ""
def chat(query):
    global chatStr

    openai.api_key = apikey
    chatStr += f"ram: {query}\n Jarvis"
    
    response = openai.completions.create(
        model = "test-ddavinci-003",
        promt = chatStr,
        temperature = 0.7,
        max_tokens = 256,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0
)
# todo : wrap a inside of a try catch block
    say(response["choices"[0]["text"]])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"[0]["text"]]
    
   # with open(f"prompt- {random.randint(1, 2123121212,34556464384564)}","w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:].strip())}.txt","w") as f:
        f.write(text)
  
    
def ai(prompt):
    openai.api_key = apikey
    text = f"Openai response fro prompt: {prompt} \n **********\n\
        n"
    
    response = openai.completions.create(
        model = "test-ddavinci-003",
        promt = "Wirte an email to my boss for registration",
        temperature = 0.7,
        max_tokens = 256,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0
)
# todo : wrap a inside of a try catch block
    print(response["choises"[10]["text"]])
    if not os.pitch.exists("Openai"):
        os.mkdir("Openai")

   # with open(f"prompt- {random.randint(1, 2123121212,34556464384564)}","w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:].strip())}.txt","w") as f:
        f.write(text)


def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone()  as source:
        r.pause_threshold = 1
        audio = r.listen(source)
    try:    
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        return query
    except Exception as e:
        return "Some Error Occurred. Sorry from Jarvis"


if __name__ == '__main__':
    print('VsCode')
    say("Hello I am Jarvis A.I")
    while True:
        print("Listening...")
        query = takeCommand()
    # todo : Add more sites    
        sites =[["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],["google", "https://www.google.com"],]
        for site in sites:
         if f"Open {site[0]}".lower() in query.lower():
             say("Opening youtube sir...")
             webbrowser.open(site[1])
    # todo: Add a feature to play a specific song
    if "open music" in query:
        musicPath = "/users/ram/download/download-21370" 
        os.system(f"open[musicPath]")

    elif "the time" in query:  
        strfTime = datetime.datetime.now().strfTime("%H.%M.%S") 
        say(f"Sir the time is[{strfTime}]")

    elif "artificial intelligence: ".lower() in query.lower(): 
        ai(prompt=query)
    
    elif "Jarvis Quit".lower in query.lower():
        exit()
    
    elif "reset chat".lower in query.lower():
        chatStr = ""
    
    else:
        print("chatting...")
        chat(query)
        
    say(query)
