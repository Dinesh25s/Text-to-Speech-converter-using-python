# import libraries#

from tkinter import *
from tkinter import ttk
from gtts import gTTS
from playsound import playsound
import os
import webbrowser



# for window instialize #

root = Tk()
root.title("SaiDinesh - TEXT_TO_SPEECH")
root.resizable(0,0)
root.geometry('500x400')
root.config(bg='gray')


#Heading
Label(root, text="TEXT_TO_SPEECH",font="arial 25 bold", bg='gray').pack()




#lable
Label(root, text="Enter Text", font='arial 15 bold', bg='gray').place(x=20, y=60)


#text variable
Msg = StringVar()


#enter text
entry_field = Entry(root, textvariable=Msg, width='50')
entry_field.place(x=20, y=100)


# define function#

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('SaiDinesh.mp3')
    playsound('SaiDinesh.mp3')


def Exit():
    root.destroy()

def Reset():
    Msg.set("")

def SaiDinesh():
    webbrowser.open_new(r"https://www.linkedin.com/in/saidinesh25/")

# define buttons
Button(root, text="PLAY", font='arial 15 bold', command= Text_to_speech,bg='green' ,width='4').place(x=25, y=140)
Button(root, text="EXIT", font='arial 15 bold', command=Exit,bg='red', width='4').place(x=100, y=140)
Button(root, text="RESET", font='arial 15 bold', command=Reset,bg='yellow', width='6').place(x=175, y=140)
Button(root,text="SaiDinesh",font="arial 20 bold",command=SaiDinesh ,bg='white smoke').pack(side= BOTTOM)

#exexute program
root.mainloop()