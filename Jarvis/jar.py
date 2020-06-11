import pyttsx3
import random
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine =pyttsx3.init()

# rate=engine.getProperty('rate')
# print(rate)
# engine.setProperty('rate',200)

def speak(audio):
    voices=engine.getProperty('voices')
    # i=random.randint(0,1)
    engine.setProperty('voice',voices[1].id)
    engine.say(audio)
    engine.runAndWait()

def time():
    Time=datetime.datetime.now().strftime('%H:%M:%S')
    speak("The current time is:")
    speak(Time)

def date():
    Date=int(datetime.datetime.now().day)
    Month=int(datetime.datetime.now().month)
    Year=int(datetime.datetime.now().year)
    speak("The current date is:")
    speak(Date)
    speak(Month)
    speak(Year)

def hour_check():
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good morning Maam")
    elif hour>=12 and hour<18:
        speak("Good afternoon Maam")
    elif hour>=18 and hour<24:
        speak("Good evening maam")
    else:
        speak("Good night maam")

def greeting():
    hour_check()
    # date()
    # time()
    speak("Jojo at your service, please tell how can i help you")

def take_cmd():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.adjust_for_ambient_noise(source, duration=1)
        # r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio,language='en-in')
        print(query)
    except Exception as e:
        print(e)
        # speak("Say that again please..")
        # return "None"
    return query

def send_mail(to_m,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    from_m='gandhemadhura@gmail.com'
    server.login(from_m)
    server.sendmail(from_m,to_m,content)
    server.close()

def screenshots():
    img=pyautogui.screenshot()
    img.save('ss.png')

def cpu():
    usage=str(psutil.cpu_percent())
    speak("cpu usage is "+usage)
    battery=psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())


if __name__ == '__main__':
    greeting()
    while True:
        que = take_cmd().lower()
        query=que.split()
        print(query)
        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'google' in query:
            print("Do you wanna wikipedia it, yes or no??")
            lis = input()
            # print(lis)
            if 'yes' in lis:
                speak("searching...")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            elif 'no' in lis:
                chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                speak("searching...")
                wb.get(chromepath).open_new_tab(query)

        elif 'mail' in query:
            try:
                speak("What message you want to send")
                content=take_cmd()
                speak("Enter the receipents mail address")
                to_m=input()
                send_mail(to_m,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Error occured could not send the email")

        elif 'cpu' in query:
            cpu()

        elif 'music' in query:
            song_dir='R:\hell-o-wood'
            songs=os.listdir(song_dir)
            i=random.randint(0, 100)
            print("in music")
            os.startfile(os.path.join(song_dir,songs[i]))

        elif 'screenshot' in query:
            screenshots()
            speak("screenshot taken")

        elif 'jokes' in query:
            jokes()

        elif 'remember' in query:
            speak("What should i remember")
            this=take_cmd()
            speak("I have to remember this "+this)
            remember=open('imp.txt','w')
            remember.write(this)
            remember.close()

        elif 'secret' in query:
            speak("Yes you did tell me to remember something")
            speak("was it..")
            remember=open('imp.txt','r')
            speak(remember.read())

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'quit' in query:
            quit()



