import pyttsx3 #for text to speech conversion
import datetime #to work with date and time
import speech_recognition as sr #translates spoken languages into text
import wikipedia #to make any search on wikipedia
import webbrowser #to allow displaying Web-based documents to users.
import os 
import pyjokes
import pyaudio
import wolframalpha
import time
import subprocess
from newsapi import NewsApiClient
import requests


engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)

def speak(audio):
    #give an audio respond "text to speech"
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    #here using date time module to wish acc to time
    hour = int(datetime.datetime.now().hour) 

    if hour>= 0 and hour<12: 
        speak("Good Morning  !") 
   
    elif hour>= 12 and hour<18: 
        speak("Good Afternoon  !")    
   
    else: 
        speak("Good Evening  !") 
    speak("i m janney, your assistent , how may i help you")  
    
def takeCommand():
    # taking command from user speech recognition
    r = sr.Recognizer() 
      
    with sr.Microphone() as source: 
          
        print("Listening...") 
        r.pause_threshold = 0.8
        audio = r.listen(source) 

    try:
        print("recognising...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said:{query} \n ")


    except Exception as e:
        print(e)
        speak("may i have your pardon please !")
        return "none"
        
    return query

def Newsin(): 
      
    # news api 
    main_url = "http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey= -----"#write api key
    # fetching data in json format 
    open= requests.get(main_url).json() 
  
    # getting all articles in a string article 
    article = open["articles"] 
  
    # empty list which will  
    # contain all trending news 
    results = [] 
      
    for ar in article: 
        results.append(ar["title"]) 
          
    for i in range(len(results)): 
          
        # printing all trending news 
        print(i + 1, results[i]) 
  
    #to read the news out loud for us                  
    speak(results)


if __name__ == "__main__":

    wishMe()

    while True:
        query = takeCommand().lower()

        # logic for executing query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
         

        elif 'open youtube' in query:
            speak("please wait.....  opening youtube")
            webbrowser.open("https://www.youtube.com/user/YouTube/videos?app=desktop")
            time.sleep(5)


        elif 'can you sing' in query:
            speak("i can't sing but i can play a song for you...  here you go ")
            webbrowser.open("https://www.youtube.com/watch?v=OC6AFSZLtnk?")
            time.sleep(10)


        elif 'open google' in query:
            speak("please wait.....  opening google")
            webbrowser.open("https://www.google.com?app=desktop")
            time.sleep(5)

        elif 'close google' in query or 'close youtube' in query or 'close instagram' in query or 'close linkedin' in query or 'close all tabs'in query:
            speak("closing... ")
            os.system("TASKKILL /F /IM chrome.exe")
            
            time.sleep(2)

            

        elif 'open instagram' in query:
            speak("please wait.....  opening instagram")
            webbrowser.open("https://www.instagram.com?app=desktop")
            time.sleep(5)

        elif 'open linkedin' in query:
            speak("please wait.....  opening linkedin")
            webbrowser.open("https://linkedin.com?app=desktop") 
            time.sleep(2)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            print(f"time is {strTime}\n")
            speak(f"time is {strTime} \n")

        elif 'open code' in query:
            speak("please wait... opening code")
            codePath = "C:\\Users\\pc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" #target path in your pc
            os.startfile(codePath)
            time.sleep(5)

        elif "open gmail" in query:
            speak("please wait.....  opening gmail")
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=wm&ogbl#inbox")
            time.sleep(5)


        elif 'open stack overflow' in query: 
            speak("Here you go to Stack Over flow.  Happy coding") 
            webbrowser.open("https://www.stackoverflow.com?app=desktop")
            time.sleep(5)

        elif 'how are you' in query: 
            speak("I am fine, Thank you") 
            speak("How are you") 
  
        elif 'fine' in query or "good" in query: 
            speak("It's good to know that your fine")

        elif 'janney' in query or 'hello' in query:
            speak("how can i help you")
        
        elif 'news' in query:
            Newsin()
        
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(f"i got a good one for you listen {joke}")
        
        elif "write a note" in query: 
            speak("What should i write") 
            note = takeCommand() 
            file = open('janney.txt', 'a') 
            file.write(note)
            speak("done!") 
          
        elif "show note" in query: 
            speak("Showing Notes") 
            file = open("janney.txt", "r")  
            print(file.read()) 
            speak(file.read(6)) 
  
        elif "sleep" in query or "wait" in query:
            speak("i will be back in 2 min")
            time.sleep(120)
            speak("i am back at your service ")
        
        elif 'exit' in query or 'quit' in query: 
            speak("Thanks for giving me your time") 
            exit()

        else:
            app_id = "-----"#write api key
            client = wolframalpha.Client(app_id) 
            res = client.query(query) 
            answer = next(res.results).text 
            print(answer)
            speak(answer)
        


        

        
            
          
        
        
            
