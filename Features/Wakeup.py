import speech_recognition as sr
import os

def Listen():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshhold = 1
        audio = r.listen(source, 0, 8) #Listening mode
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language = "en")
        
    except:
        # var = print("Please say again..")
        return  print('Please say again..')#This portion may be vulnerable
    
    query = str(query).lower()
    print(query)
    return query

def WakeupDetected():
    query = Listen().lower()
    
    if "wake up" in query:
        os.startfile(r"C:\Users\CHANDRIMA\Documents\New folder (2)\AI\main.py")
        
    else:
        pass
        
while True:
    WakeupDetected()