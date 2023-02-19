from Body.Speak import Speak
from Body.Listen import Listen

def MainExe():
    Speak("Main Execution Has Been Started.")
    while True:
        
        query = Listen()
        
        if "hello" in query:
            Speak('Hi! I am Jarvis')
            
        elif "bye" in query:
            Speak("Bye Sir.")
            break