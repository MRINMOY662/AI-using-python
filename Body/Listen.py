#Hindi or English - Command
#English

#Step - 1
#pip install googletrans==3.1.0a0

#Step - 2
# Three functions
# 1 - Listen Function
# 2 - English Translation
# 3 - Connect

import speech_recognition as sr #pip install speechrecognition
from googletrans import Translator

# 1 - Listen : Hindi or English

def Listen():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshhold = 1
        audio = r.listen(source, 0, 9) #Listening mode
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language = "en")
        
    except:
        # var = print("Please say again..")
        return  ""#This portion may be vulnerable
    
    query = str(query).lower()
    return query
    
# print(Listen())

# 2 - Translation

def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"User: {data}.")
    return data

# 3 - Connect

def MicExecution():
    query = Listen()
    data = TranslationHinToEng(query)
    return data

