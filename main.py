import pandas as pd
import numpy as np
import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as audio
import speech_recognition as input
import threading
import string
import nltk
import random

engine = audio.init()
Voices = engine.getProperty("voices")
print(Voices)

engine.setProperty("voice", Voices[0].id)


def speak(word):
    engine.say(word)
    engine.runAndWait()


bot = ChatBot("VENOM")

# with open('dialogs.txt', 'r') as file:
#     commu = file.read()
commu = [
    'hello!!',
    'hi there',
    'Tell me your name.',
    'I am venom and I am Programmed by Shivam.',
    'how are you',
    'i am doing great these days',
    'THANK YOU',
    'IN WHICH CITY YOU LIVE ?',
    'I LIVE IN BULANDSHAHR',
    'IN WHICH LANGUAGE YOU TALK ?',
    'I MOSTLY TALK IN ENGLISH',
    'Tell me your favorite Teacher.',
    'My favorite teacher is Miss. Parul.',
    'Most cutest teacher in Dronacharya college',
    'That is Miss. Parul'
]

trainer = ListTrainer(bot)
#
# # # now training the bot with the help of trainer.
#
trainer.train(commu)
#
# answer = bot.get_response("what is your name?")
# print(answer)
print("Talk to Bot")

# while True:
#     query = input()
#     if query == 'exit':
#         break
#     else:
#         answer = bot.get_response(query)
#         print("bot : ", answer)

main = Tk()

main.geometry("470x550")
BG_GRAY = "#FCDFFF"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"
FONT_COLOR = "#C8B560"

main.title("VENOM")


# take query from user and convert into string

def takequery():
    sr = input.Recognizer()
    sr.pause_threshold = 1
    print("I am listening.....")
    with input.Microphone() as micro:
        try:
            listen = sr.listen(micro)
            query = sr.recognize_google(listen, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            send()
        except Exception as e:
            print(e)
            print('not recognized')


def send():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "You: " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "Bot: " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)


frame = Frame(main)

head_label = Label(main, bg=BG_COLOR, fg=TEXT_COLOR, text="WELCOME TO MY WORLD", font=FONT_BOLD, pady=10)
head_label.place(relwidth=1)

line = Label(main, width=450, bg=FONT_COLOR)
line.place(relwidth=1, rely=0.07, relheight=0.012)

text_widget = Text(main, width=80, height=80, bg=TEXT_COLOR, fg=BG_COLOR, font=("VERDANA", 20), padx=5, pady=5)
text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
text_widget.configure(cursor="arrow", state=DISABLED)
sc = Scrollbar(text_widget)
msgs = Listbox(text_widget, width=80, height=20, yscrollcommand=sc.set)
sc.place(relheight=1, relx=0.974)
sc.configure(command=text_widget.yview)
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
text_widget.pack()

bottom_label = Label(main, bg=BG_COLOR, height=80)
bottom_label.place(relwidth=1, rely=0.825)

textF = Entry(bottom_label, bg=BG_GRAY, fg="#000000", font=("VERDANA", 15))
textF.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
textF.pack(fill=X, pady=5)

send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg="#34282C", fg="#FFFFFF", command=send)
send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
send_button.pack(pady=5)


# creating enter key enabled
def enter_function(event):
    send_button.invoke()


textF.bind("<Return>", enter_function)


def repeatevent():
    while True:
        takequery()


t = threading.Thread(target=repeatevent)

t.start()

main.mainloop()
