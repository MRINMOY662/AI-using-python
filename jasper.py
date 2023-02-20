from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
from Body.Listen import MicExecution
print(">> Starting the Jasper : Wait For Some Seconds.")
from Body.Speak import Speak
from Features.Clap import Tester
print(">> Starting the Jasper : Wait For Some Seconds.")

def MainExecution():
    
    Speak("Hello Sir")
    Speak("I'm Jasper, I'm ready to assist you Sir.")
    while True:
        
        Data = MicExecution()
        Data = str(Data)
        
        if len(Data) < 3:
            pass
        
        elif "turn on the tv" in Data: # Pattern for specific command
            Speak("Ok...Turning on the Android TV")
        
        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionsAnswer(Data)
            
        # else:
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


