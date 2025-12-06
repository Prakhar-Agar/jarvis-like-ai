import speech_recognition as sr
import webbrowser
import pyttsx3 
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsAPI = "0a696aa74df74158a4661f021f324a9e"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open gfg" in c.lower():
        webbrowser.open("https://www.geeksforgeeks.org")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsAPI}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles',[])
            for article in articles:
                speak(article['title'])

    
    # speak(c)
if __name__=="__main__":
    speak("Initializing Jarvis......")
    while True:
        # listen for the wake word "Jarvis"
        # obtain audio from the microphone
        
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
                print("Recognizing")
            word = recognizer.recognize_google(audio)
            # print(word)
            if (word.lower() == "jarvis"):
                speak("Yes Sir")
                #listen for command
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = recognizer.listen(source, timeout=4, phrase_time_limit=1)
                    command = recognizer.recognize_google(audio)

                    processCommand(command)                                              #9:48:12 time on yt
            if (word.lower() == "exit"):
                break
        except Exception as e:
            print(f"Error: {e}")
    speak("Exiting Jarvis interface")
    print("program exiting...")