import email
from turtle import width
from pyparsing import nums
import pyttsx3
import speech_recognition as sr
from datetime import datetime
import wikipedia
from required_data import *
import os
import time
from pyfiglet import Figlet
import shutil
import webbrowser
import smtplib
import speedtest


print()
# # Jarvis Heading
f = Figlet(font='basic')
width = shutil.get_terminal_size().columns


def DrawText(text, center=True):
    if center:
        print(*[x.center(width)
              for x in f.renderText(text).split("\n")], sep="\n")
    else:
        print(f.renderText(text))


DrawText('JARVIS', center=True)
print("~"*width)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
j = "Jarvis: "
# Functions


def speak(audio):
    engine.setProperty("rate", 180)
    engine.say(audio)
    engine.runAndWait()


# speak("Welcome to Jarvis Advanced AI Program.")
# speak("You can communicate through both text and speech.")

def wishMe():
    '''Wishes the User'''

    hour = int(datetime.now().hour)
    intro = "How may I help you?"
    if 0 <= hour < 12:
        print("\n" + j + "Good Morning Sir, Jarvis Here. " + intro)
        speak("Good Morning Sir, Jarvis Here. " + intro)
    elif 12 <= hour < 18:
        print("\n" + j + "Good Afternoon Sir, Jarvis Here. " + intro)
        speak("Good Afternoon Sir, Jarvis Here. " + intro)
    elif 18 <= hour < 24:
        print("\n" + j + "Good Evening Sir, Jarvis Here. " + intro)
        speak("Good Evening Sir, Jarvis Here. " + intro)


# Speech to Text
def takeCommand():
    '''Takes speech inputs and returns string outputs'''

    r = sr.Recognizer()

    with sr.Microphone() as speechSource:
        print("\n" + j + "Listening...")
        r.pause_threshold = 1
        audio = r.listen(speechSource)

    try:
        print(j + "Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"{j}User said: {query}\n")

    except Exception as e:
        print(j + "Say that again please!\n")
        return "None"
    return query

# Ignore this xD
def mail():
    # for i in emails:
    # a = "email to {user}"
    # b = a.format(user = i)

    # if b in query:
    #     ded = "Hahaha, Email Service not available because no Password Leak XDXD Die Laul."
    #     print(j + ded)
    #     speak(ded)
    #     try:
    #         to_user_email = emails[i]
    #         speak(j + "What message should I send?")
    #         content = takeCommand()
    #         sendEmail(to_user_email, content)

    #         print(f"Email sent to {i.capitalize()}.")
    #         speak(f"Email sent to {i.capitalize()}.")
    #     except Exception as e:
    #         speak(j + "Sorry sir, I'm not able to deliver your email.")

    # For Sending Email
    # def sendEmail(to, content):
    #     server = smtplib.SMTP('smtp.gmail.com', 587)
    #     server.ehlo()
    #     server.starttls()
    #     server.login('ramanbhardwaj2005@gmail.com', 'xdxd')
    #     server.sendmail('ramanbhardwaj2005@gmail.com', to, content)
    #     server.close()
    pass


def speedTest():
    pass


# ______________ Main Code ______________
if __name__ == "__main__":
    while True:
        speak("Enter the mode in which you want to communicate with.")
        print("\nType 'Text mode' or 'Speech mode'.")
        mode = input("\nEnter Mode: ").lower()
        query = None

        if 'text mode' in mode:
            print("\nEntering Text Mode...\n")
            print("________________TEXT MODE ACTIVATED________________")
            wishMe()
            print("\n-> Type 'Help' to learn more about me.")
            while True:
                query = input("\nEnter Command: \n>> ").lower()
                # Wikipedia
                if 'wikipedia' in query:
                    # Getting the main word to search in Wikipedia
                    query = query.replace('wikipedia', '')
                    query_list = query.split()

                    if 'in' in query_list:
                        query = query.replace('in', '')
                    if 'at' in query_list:
                        query = query.replace('at', '')
                    if 'search' in query_list:
                        query = query.replace('search', '')
                    if 'on' in query_list:
                        query = query.replace('on', '')

                    print(f"\n{j}Searching in Wikipedia...")
                    speak("Searching in Wikipedia.")

                    # Getting search results in 3 lines
                    try:
                        results = wikipedia.summary(query.capitalize(), sentences=3)
                    except Exception as e:
                        print(j + "Wikipedia not found.")
                        speak("Wikipedia not found.")

                    # Printing Search results
                    acc = "According to Wikipedia: \n"
                    print(j + acc)
                    speak(acc)
                    print(j + results)
                    speak(results)

                # Opening Sites
                elif 'open youtube' in query:
                    print(j + "Opening YouTube...")
                    webbrowser.open("youtube.com")

                elif 'open google' in query:
                    print(j + "Opening Google...")
                    webbrowser.open("google.com")

                elif 'open Animix' in query or 'open our site' in query:
                    print(j + "Opening Animix...")
                    webbrowser.open("lol8585.github.io/Animix/home.html")

                # Closing Sites
                elif 'close youtube' in query or 'close google' in query or 'close animix' in query:
                    os.system("taskkill /f / im msedge.exe")
                    os.system("taskkill /f / im chrome.exe")

                # Playing Music
                elif 'play music' in query:
                    music_loc = 'music'
                    songs = os.listdir(music_loc)
                    print("Playing " + songs[0])
                    os.startfile(os.path.join(music_loc, songs[0]))
                
                # Close Music
                elif 'close music' in query:
                    os.system("TASKKILL /F /IM Music.UI.exe")
                    time.sleep(10)
                    print(j + "Music Closed.")

                # Time
                elif 'the time' in query:
                    strTime = datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir, the time is {strTime}")

                # Opening Apps
                elif 'open code' in query:
                    code_path = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    print(j + "Opening Visual Studio Code...")
                    os.startfile(code_path)
                elif 'open chrome' in query:
                    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                    print(j + "Opening Chrome...")
                    os.startfile(chrome_path)
                elif 'open telegram' in query:
                    telegram_path = "C:\\Users\\HP\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
                    print(j + "Opening Telegram...")
                    os.startfile(telegram_path)
                elif 'open unity' in query:
                    unity_path = "C:\\Program Files\\Unity Hub\\Unity Hub.exe"
                    print(j + "Opening Unity...")
                    os.startfile(unity_path)

                # Closing Apps
                elif 'close code' in query:
                    os.system("TASKKILL /F /IM Code.exe")
                    time.sleep(10)
                elif 'close chrome' in query:
                    os.system("TASKKILL /F /IM Chrome.exe")
                    time.sleep(10)
                elif 'close telegram' in query:
                    os.system("TASKKILL /F /IM Telegram.exe")
                    time.sleep(10)
                elif 'close unity' in query:
                    os.system("TASKKILL /F /IM Unity Hub.exe")
                    time.sleep(10)

                # Sending Emails
                elif 'email' in query:
                    ded = "Hahaha, Email Service not available because no Password Leak XDXD Die Laul."
                    print(j + ded)
                    speak(ded)

                # Help
                elif 'help' in query:
                    print("\nAll Commands for Jarvis:\n")
                    print("Feature                                             Command")
                    print(">> Change Voice of this AI                        -> set voice 1 to 4")
                    print(">> Search anything in wikipedia                   -> search 'something' in wikipedia")
                    print(">> Play Music                                     -> play music")
                    print(">> Open Animix, Code, YT, Google, Telegram, Unity -> open 'any app given'")
                    print(">> Ask Time                                       -> What's the time jarvis?")
                    print(">> Send Email                                     -> send email to 'someone'")

                # Changing Voice
                elif 'set voice 1' in query:
                    engine.setProperty('voice', voices[0].id)
                elif 'set voice 2' in query:
                    engine.setProperty('voice', voices[1].id)
                elif 'set voice 3' in query:
                    engine.setProperty('voice', voices[2].id)
                elif 'set voice 4' in query:
                    engine.setProperty('voice', voices[3].id)
                
                # Making AI Speak Something
                elif 'say' in query:
                    query = query.replace("say", "")
                    print("\n" + j + query.capitalize())
                    speak(query)

                else:
                    speak("Command not available. Try Again")

        elif 'speech mode' in mode:
            wishMe()
            print("\n-> Say 'Help' to learn more about me.")
            while True:
                query = takeCommand().lower()
                # Wikipedia
                if 'wikipedia' in query:
                    # Getting the main word to search in Wikipedia
                    query = query.replace('wikipedia', '')
                    query_list = query.split()

                    if 'in' in query_list:
                        query = query.replace('in', '')
                    if 'at' in query_list:
                        query = query.replace('at', '')
                    if 'search' in query_list:
                        query = query.replace('search', '')
                    if 'on' in query_list:
                        query = query.replace('on', '')

                    print(f"\n{j}Searching in Wikipedia...")
                    speak("Searching in Wikipedia.")

                    # Getting search results in 3 lines
                    try:
                        results = wikipedia.summary(query.capitalize(), sentences=3)
                    except Exception as e:
                        print(j + "Wikipedia not found.")
                        speak("Wikipedia not found.")

                    # Printing Search results
                    acc = "According to Wikipedia: \n"
                    print(j + acc)
                    speak(acc)
                    print(j + results)
                    speak(results)

                # Opening Sites
                elif 'open youtube' in query:
                    print(j + "Opening YouTube...")
                    webbrowser.open("youtube.com")

                elif 'open google' in query:
                    print(j + "Opening Google...")
                    webbrowser.open("google.com")

                elif 'open Animix' in query or 'open our site' in query:
                    print(j + "Opening Animix...")
                    webbrowser.open("lol8585.github.io/Animix/home.html")

                # Closing Sites
                elif 'close youtube' in query or 'close google' in query or 'close animix' in query:
                    os.system("taskkill /f / im msedge.exe")
                    os.system("taskkill /f / im chrome.exe")

                # Playing Music
                elif 'play music' in query:
                    music_loc = 'music'
                    songs = os.listdir(music_loc)
                    print("Playing " + songs[0])
                    os.startfile(os.path.join(music_loc, songs[0]))
                
                # Close Music
                elif 'close music' in query:
                    os.system("TASKKILL /F /IM Music.UI.exe")
                    time.sleep(10)
                    print(j + "Music Closed.")

                # Time
                elif 'the time' in query:
                    strTime = datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir, the time is {strTime}")

                # Opening Apps
                elif 'open code' in query:
                    code_path = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    print(j + "Opening Visual Studio Code...")
                    os.startfile(code_path)
                elif 'open chrome' in query:
                    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                    print(j + "Opening Chrome...")
                    os.startfile(chrome_path)
                elif 'open telegram' in query:
                    telegram_path = "C:\\Users\\HP\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
                    print(j + "Opening Telegram...")
                    os.startfile(telegram_path)
                elif 'open unity' in query:
                    unity_path = "C:\\Program Files\\Unity Hub\\Unity Hub.exe"
                    print(j + "Opening Unity...")
                    os.startfile(unity_path)

                # Closing Apps
                elif 'close code' in query:
                    os.system("TASKKILL /F /IM Code.exe")
                    time.sleep(10)
                elif 'close chrome' in query:
                    os.system("TASKKILL /F /IM Chrome.exe")
                    time.sleep(10)
                elif 'close telegram' in query:
                    os.system("TASKKILL /F /IM Telegram.exe")
                    time.sleep(10)
                elif 'close unity' in query:
                    os.system("TASKKILL /F /IM Unity Hub.exe")
                    time.sleep(10)
                
                # Sending Emails
                elif 'email' in query:
                    ded = "Hahaha, Email Service not available because no Password Leak XDXD Die Laul."
                    print(j + ded)
                    speak(ded)

                elif 'help' in query:
                    print("\nAll Commands for Jarvis:\n")
                    print(       "Feature                                           Command")
                    print(">> Change Voice of this AI                        -> set voice 1 to 4")
                    print(">> Search anything in wikipedia                   -> search 'something' in wikipedia")
                    print(">> Play Music                                     -> play music")
                    print(">> Open Animix, Code, YT, Google, Telegram, Unity -> open 'any app given'")
                    print(">> Ask Time                                       -> What's the time jarvis?")
                    print(">> Send Email                                     -> send email to 'someone'")

                 # Changing Voice
                elif 'set voice 1' in query:
                    engine.setProperty('voice', voices[0].id)
                elif 'set voice 2' in query:
                    engine.setProperty('voice', voices[1].id)
                elif 'set voice 3' in query:
                    engine.setProperty('voice', voices[2].id)
                elif 'set voice 4' in query:
                    engine.setProperty('voice', voices[3].id)
                
                # Making AI Speak Something
                elif 'say' in query:
                    query = query.replace("say", "")
                    print("\n" + j + query.capitalize())
                    speak(query)

                
                else:
                    speak("Command not available. Try Again.")
        else:
            speak("Enter the Correct mode.")