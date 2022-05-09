import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
from pyautogui import *
import psutil
import requests
import pyjokes
import os
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning sir")

    elif hour >= 12 and hour < 18:
        speak("good afternoon sir")

    else:
        speak("good evening")

    speak(" i am your desktop assistant. please tell me how may i assist you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said, {query}\n")
    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"
    return query


if __name__ == '__main__':
    greet()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:                                        
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:                                   
            webbrowser.open("https://youtube.com")
        
        elif 'open github' in query:
            webbrowser.open("https://github.com/")           


        elif 'the time' in query:                                      
            Time = datetime.datetime.now().strftime("%I:%M:%S")
            speak(f"sir, the time is {Time}")

        elif 'the date' in query: 
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            speak(f"sir, the date is {date}")

        elif 'take screenshot' in query:
            time.sleep(3) 
            wow = screenshot()
            wow.save(r'C:\Users\shrey\OneDrive\Pictures\Screenshots\hello.png')

        elif 'temperature' in query:
            city = "mumbai"
            res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=16f0afad2fd9e18b7aee9582e8ce650b&units=metric").json()
            temp2 = res["main"]["temp"]
            speak(f"temperature is {format(temp2)} degree Celsius")
        
        elif 'weather' in query:
            city = "mumbai"
            res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=16f0afad2fd9e18b7aee9582e8ce650b&units=metric").json()
            temp1 = res["weather"][0]["description"]
            speak(f"The weather is {format(temp1)}")

        elif 'netflix' in query:
            webbrowser.open("https://www.netflix.com/browse")
        
        elif 'joke' in query:
            speak(pyjokes.get_joke('en'))

        elif "cpu" in query:
            speak(f"cpu is at {str(psutil.cpu_percent())}")

        elif 'geeks' in query:
            webbrowser.open('http://geeksforgeeks.org/')

        elif 'excel' in query:
            os.chdir(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs')
            os.system('start excel')

        elif 'powerpoint' in query:
            os.chdir(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs')
            os.system("start powerpnt")

        elif 'word' in query:
            os.chdir(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs')
            os.system('start winword')

        elif 'notepad' in query:
            os.system('notepad')

        elif 'exit' in query:
            exit()

        elif 'command prompt' in query:
            os.system('cmd')

        elif 'powershell' in query:
            os.system('powershell')

        elif 'classroom' in query:
            webbrowser.open("https://classroom.google.com/u/1/c/MzE0MTM3NzMwODI3")

        elif 'drive' in query:
            webbrowser.open("https://drive.google.com/drive/u/0/my-drive")

        elif 'guitar' in query:
            webbrowser.open("https://lms.shankarmahadevanacademy.com/lms/myhome/")

        elif 'translate' in query:
            webbrowser.open("https://translate.google.com/")

        elif 'whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif 'chess meeting' in query:
            webbrowser.open("https://us04web.zoom.us/j/6098474080?pwd=bk5MZjVibGFEeFZidjhFSnJDSFFkUT09")

        elif 'text shortner' in query:
            webbrowser.open("https://quillbot.com/summarize")

        elif 'shutdown' in query:
            os.system('shutdown /s /t 1')

        elif 'alan walker' in query:
            webbrowser.open("https://www.youtube.com/watch?v=yznImFnedmw")
        
        elif 'rickroll' in query:
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

        elif 'python to exe' in query:
            speak("Enter path in the terminal")
            a = input("Enter path to your python file: ")
            os.system(f'pyinstaller --onefile {a}')

        elif 'calculator' in query:
            os.system(r'python -u C:\Users\shrey\OneDrive\Desktop\Code\Python\calculator.py')
            speak("opened calculator")
            continue
        
        elif 'to do' in query:
            os.system(r'''python -u "C:\Users\shrey\OneDrive\Desktop\Code\Python\todo App\todo_list_app.py"''')
