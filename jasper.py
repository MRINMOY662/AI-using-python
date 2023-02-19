from Brain.AIBrain import ReplyBrain
from Body.Listen import MicExecution
print(">> Starting the Jasper : Wait For Some Seconds.")
from Body.Speak import Speak
from Features.Clap import Tester
print(">> Starting the Jasper : Wait For Some Seconds.")

def MainExecution():
    
    Speak("Hello Sir")
    Speak("I'm Jarvis, I'm ready to assist you Sir.")
    while True:
        
        Data = MicExecution()
        Data = str(Data)
        Reply = ReplyBrain(Data)
        Speak(Reply)
        

def ClapDetect():
    query = Tester()
    if "True-Mic" in query:
        print("")
        print(">> Clap Detected !! >>")
        print("")
        MainExecution()
    else:
        pass
ClapDetect()


