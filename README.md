🤖 Rule-Based AI Python Chatbot

A smart, interactive command-line interface (CLI) chatbot built with Python. This project demonstrates foundational programming concepts including real-time data handling, string manipulation, dictionary-based memory retrieval, and intent matching.

---

 ✨ Features

* 🌞 Time-Aware Greetings: Automatically detects the user's local system time to deliver personalized "Good Morning", "Good Afternoon", "Good Evening", or "Good Night" greetings.
* 🧠 Context-Based Memory: Uses a key-value dictionary structure to map user queries to accurate responses instantly.
* 🔍 Flexible Intent Matching: Converts user input to lowercase and matches substrings, allowing the bot to understand queries even if they are part of a longer sentence.
* 🗣️ Bilingual Support (Hinglish): Programmed to recognize and respond to programming questions in a mix of Hindi and English (e.g., explaining Python functions).
* 🔄 Continuous Execution Loop: Runs seamlessly in the terminal until the user explicitly types 'bye' to exit.

---

 🛠️ Tech Stack & Concepts Demonstrated

* Language: Python 3
* Standard Libraries: datetime, time
* Core Concepts: 
  * Conditional Logic (if-elif-else)
  * Infinite while loops with control statements (break)
  * Dictionary manipulation and lookup optimization
  * Functional programming (def structures with parameters and return values)

---

 🚀 How to Run the Project Local Layout

To test this chatbot on your local machine, make sure you have Python installed.

1. Clone this repository to your local machine:

   git clone https://github.com
   
2. Navigate into the project directory:

   cd PersonalChatAssistant
   

3. Execute the script via terminal:
  
   python main.py
   
---

📋 Sample Conversations

Enter your name: Alex
Good afternoon, Alex
Namaste! Welcome to your Chatbot.
You can ask me basic questions, type 'bye' to exit from the bot

please ask your question: Hello there!
bot response: Hi, Welcome. How can I help you?

please ask your question: functions ky hote hai?
bot response: A function is a block of code which only runs when it is called. It can return data as a result. It helps avoid code repetition.

please ask your question: can you motivate me?
bot response: Keep going. Every bug of your project makes you a better developer.

please ask your question: bye chatbot
bot response: Bye! Have a great day.
