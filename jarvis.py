import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import smtplib

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=datetime.datetime.now().hour
    if(hour>=1 and hour<=12):
        speak("good morning")
    elif(hour>=13 and hour<=18):
        speak("good afternoon")
    else:
        speak("good evening")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"U said: {query}\n")  #User query will be printed.

    except Exception as e:  
        print("Sorry i coudn't make that out")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query


def email(to,connect):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("AC.ashmi.AC@gmail.com","kiminonawa")
    server.sendmail("AC.ashmi.AC@gmail.com",to,connect)
    server.close()


rate = engine.getProperty('rate')   # getting details of current speaking rate                    
engine.setProperty('rate', 125)     # setting up new voice rate

if __name__=="__main__" :
    wishme()
    while True:
        query = takecommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif 'ok google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "AC.ashmi.AC@gmail.com"    
                email(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")    
        elif 'quit' in query:
            speak("bye bye")
            speak("i'll go to sleep now")
            quit() 


