import pyttsx3
import datetime
import speech_recognition as sr 
import pyaudio
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour == 0 and hour<12:
        speak("Good morning!")
    elif hour >=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")

def takeCommand():             
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recoganizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said  {query}\n" )

    except Exception as e:
        print(e)
        print("Say that once again..")
        return "none"

    return query

if __name__ == "__main__":
    wishme()
    speak("Hello sir I am your virtual assistant Please tell me how may help you")

    while True:
        query= takeCommand().lower()

   #logic for execution based on query

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open yahoo' in query:
            webbrowser.open("wekipedia.com")
        
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'open google drive' in query:
            webbrowser.open("googledrive.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\GOURAV\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\GOURAV\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'open chrome' in query:
            chrome = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome)