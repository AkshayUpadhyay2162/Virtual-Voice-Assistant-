import pyttsx3
import datetime
import wikipedia
import os
import webbrowser
import speech_recognition as sr
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    '''
    This function is used to produce given text in the form of voice.
    '''
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good morning, Akshay")
    elif hour>=12 and hour<16:
        speak("Good afternoon, Akshay")
    else:
        speak("Good evening, Akshay")
    speak("I am Jarvis sir. Please tell me how may i help you")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_email@gmail.com','your_password')
    server.sendmail('your_email@gmail.com', to, content)
    server.close()
def takeCommands(): 
        # It takes microphone input from the user and returns string output.
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.non_speaking_duration = 0.8
            # r.energy_threshold = 400
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in',)
            print(f"You said: {query}\n")
            
        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
        return query
                
if __name__ == "__main__":
    wishMe()
    while True:
        query1 = takeCommands().lower()
        if 'wikipedia' in query1:
            speak("Searching wikipedia...")
            query1 = query1.replace("wikipedia","")
            results = wikipedia.summary(query1, sentences=2)
            print(results)
            speak(results)
        
        elif 'type' in query1:
            print(query1)    
        
        elif 'hello' in query1:
            speak("Hello Akshay sir")
            
        elif 'what is your name' in query1:
            speak('My name is Jarvis sir. I am here for your help')
            
        elif 'open youtube' in query1:
            speak("opening youtube")
            webbrowser.open('youtube.com')
            
        elif 'open google' in query1:
            speak("opening google")
            webbrowser.open('google.com')
            
        elif 'open stackoverflow' in query1:
            speak("opening stackoverflow")
            webbrowser.open('stackoverflow.com')
        
        elif 'open geeksforgeeks' in query1:
            speak("opening geeksforgeeks")
            webbrowser.open('geeksforgeeks.com')
        
        elif 'open facebook' in query1:
            speak("opening facebook")
            webbrowser.open('facebook.com')
        
        elif 'play music' in query1:
            music_dir = 'E:\\Songs'
            songs = os.listdir(music_dir)   
            print("Playing songs")
            speak("playing songs")
            os.startfile(os.path.join(music_dir,songs[0]))
            
        elif 'the time' in query1:
            Time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {Time}")
            
        elif 'open chrome' in query1:
            chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            speak("opening google chrome")
            os.startfile(chrome_path)
            
        elif 'open visual studio' in query1:
            code_path = "C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("opening visual studio code")
            os.startfile(code_path) 
            
        elif 'send email' in query1:
            try:
                print("What should i send sir?")
                speak("What should i send sir?")
                content = takeCommands()
                to = "reciever_email@gmail.com"
                sendEmail(to, content)
                # print("Email has been sent successfully")
                speak("Email has been sent successfully")
                
            except Exception as e:
                print(e)
                speak("Sorry sir, i couldn't send the email. please try again")
        
                
            
        elif 'exit' in query1:
            break
    speak("Thank you Sir, Have a good day")  
        