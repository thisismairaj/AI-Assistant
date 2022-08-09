from audioop import tostereo
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import smtplib
import pywhatkit
import pyjokes

engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices')

def changevoice(input=1):
    if 'female' in input:
        engine.setProperty('voice', voices[1].id)
    elif 'male' in input:
        engine.setProperty('voice', voices[0].id)
    
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'change voice' in query:
            speak("Do you want male voice or female voice?")
            changevoice(takeCommand().lower())
            speak("Voice changed")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))
        elif 'play' in query or 'show' in query or 'watch' in query or 'youtube' in query:
            song = query.replace('play', '')
            song = query.replace('watch', '')
            song = query.replace('youtube', '')
            song = query.replace('watch', '')

            pywhatkit.playonyt(song)

        elif 'joke' in query:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())
            
        elif 'time' in query or 'date' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\muham\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Opening Visual Studio Code")
            os.startfile(codePath)
        elif 'search' in query:
            keyword = query.replace('search', '')
            speak('Searching'+ keyword)
            pywhatkit.search(keyword)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")
        elif 'end program' in query or 'quit jarvis' in query or 'bye jarvis' in query:
            speak("Goodbye Sir. Have a nice day")
            exit()