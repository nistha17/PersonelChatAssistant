# Rule Based AI Python Chatbot

import datetime
import time

name= input("Enter your name:")
presentHour= datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print("Good morning,",name)
elif 11 <= presentHour <= 16:
    print("Good afternoon,",name)  
elif 16 <= presentHour <= 19:
    print("Good evening,",name)  
else:
    print("Good night,",name)

print("Namaste!Welcome to your Chatbot.")
print("You can ask me basic question,type 'bye' to exit from the bot")

# Chatbot Memory Creation [dictionary of responses]

responses = {
    "hello":"Hi,Welcome.how can i help you?",
    "how are you": "I am very fine. Thank you",
    "Who are you":"Iam smart AI Chatbot",
    "motivate me":"Keep going.Every bug of your project makes you a better developer",
    "happy":"Great to hear that.",
    "functions ky hote hai":"A function is a block of code which only runs when it is called.It can return data as a result.it helps avoiding code repetition"
    }

# method/Function to get response of ChatBot

def getResponseBot(userQuestion):
    userQuestion= userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
        
    return "I am not able to tell that yet. Mai jldi sikh lunga ."


 # Take user input

while True:
    userInput=input("please ask your question:")
     
    if "bye" in userInput.lower():
        print("bot response:Bye! Have a great day.")
        break
     
    reply=getResponseBot(userInput)
    print("bot response:",reply)

     



