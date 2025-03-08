# # import pyttsx
# #
# # # initialisation
# # engine = pyttsx.init()
# #
# # # testing
# # engine.say("My first code on text-to-speech")
# # engine.say("Thank you, Geeksforgeeks")
# # engine.runAndWait()
# # from collections import deque
# #
# #
# # class Stack:
# #     def __init__(self):
# #         self.container=deque()
# #     def push(self,val):
# #         return  self.container.append(val)
# #     def pop(self):
# #         return self.container.pop()
# #     def peek(self):
# #         return self.container[-1]
# #     def is_empty(self):
# #         return len(self.container)==0
# #     def size(self):
# #         return len(self.container)
# # def reverse_string(s):
# #     stack=Stack()
# #     for char in s:
# #         stack.push(char)
# # #     rst=""
# # #     while stack.size()!=0:
# # #         rst +=stack.pop()
# #
# #
# # # if __name__ == '__main__':
# # #     print(reverse_string("we are willing to devote a greate deal of time to study mathematics"))
# #
# #
# # from collections import deque
# #
# # class Stack:
# #     def __init__(self):
# #         self.container = deque()
# #
# #     def push(self, val):
# #         self.container.append(val)
# #
# #     def pop(self):
# #         return self.container.pop()
# #
# #     def peek(self):
# #         return self.container[-1]
# #
# #     def is_empty(self):
# #         return len(self.container) == 0
# #
# #     def size(self):
# #         return len(self.container)
# #
# # def reverse_string(s):
# #     stack = Stack()
# #
# #     for ch in s:
# #         stack.push(ch)
# #
# #     rstr = ''
# #     while stack.size()!=0:
# #         rstr += stack.pop()
# #
# #     return rstr
# #
# #
# # if __name__ == '__main__':
# #     print(reverse_string("We will conquere COVI-19"))
# #     print(reverse_string("I am the king"))
#
# #
# # def dig_to_str(i):
# #     digit="0123456789"
# #     if i==0:
# #         return "0"
# #     result=""
# #     while i>0:
# #         result=digit[i%10]+result
# #         i=i//10
# #     return result
# #
# # dig_to_str(431)
# #
# # l=[1,2,3,4,5]
# # for i in range(0,len(l)+1):
# #     for j in range(i+1,len(l)):
# #         print("({},{})".format(l[i],l[j]))
#
# L=[1,2,3,4,5]
# for i in range(0,len(L)//2):
#     other=len(L)-i-1
#     temp=L[i]
#     L[i]=L[other]
#     L[other]=temp
# print(L)
from numpy.ma.core import filled
from numpy.ma.extras import column_stack

BACKGROUND_COLOR = "#B1DDC6"
import random
import pandas
from tkinter import *
import pyttsx3

import speech_recognition as sr
data = pandas.read_csv("hungarian_sentences_100.csv")
to_learn = data.to_dict(orient="records")
current_card={}

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)

    canvas.itemconfig(card_title,text="Hungarian",fill="black")
    canvas.itemconfig(card_word,text=current_card["Hungarian"],fill="black")
    canvas.itemconfig(card_background,image=front_image)

    engine=pyttsx3.init()
    engine.say(current_card["Hungarian"])
    engine.setProperty("rate",1)
    engine.runAndWait()


    flip_timer=window.after(3000,func=flip_card)



def flip_card():
    canvas.itemconfig(card_title,text="English" ,fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=back_image)














window=Tk()
window.title("Learn Hungarian")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,func=flip_card)
canvas=Canvas(width=800,height=526)

back_image=PhotoImage(file="card_back.png")
# canvas.create_image(image=back_image)
front_image=PhotoImage(file="card_front.png")
card_background=canvas.create_image(400,263,image=front_image)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_title=canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
card_word=canvas.create_text(400,263,text="",font=("Ariel",30,"bold"))

canvas.grid(row=0,column=0,columnspan=2)
wrong_image=PhotoImage(file="wrong.png")
unknown_button=Button(image=wrong_image,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)
correct_image=PhotoImage(file="right.png")
correct_button=Button(image=correct_image,highlightthickness= 1,command=next_card)
correct_button.grid(row=1,column=1)


next_card()






window.mainloop()