print("Local SMS")
print("this is still in prototype form")
from tkinter import *
import random

master = Tk()

master.config(width=500, height=500)
master.maxsize(300,400);

master.title("Chat Room for people to chat easly than ever")
master.configure(background="white")

global username
global contents
global messagelabel
global messages
global messagestext
global UserColour
global Select
global StayTyping
messagestext = ""
username = ""
f = open("SMS.txt", "w")
f.write(" ")
f.close()

Select = 0
total = 0
StayTyping = 0

while total < 300:
    a = random.randint(0,255)
    b = random.randint(0,255)
    c = random.randint(0,255)
    total = a + b + c
UserColour =  "#%02x%02x%02x" % (a, b, c)

def enter(event):
    global Select
    if Select == 0:
        username()
    if Select == 1:
        send()

def send():
    global contents, UserColour
    f = open("SMS.txt", "w")
    g = open("Colour.txt", "a")
    f.write(username + ": " + contents.get() + " " + username + ": " + contents.get() + "\n")
    g.write(str(UserColour) + "\n")
    f.close()
    g.close()
    contents.destroy()
    contents = Entry(master)
    contents.place(width=250,height=20, relx = 0.4175, rely = 0.975, anchor = CENTER)

def username():
    global update
    global username
    global contents
    global messages
    global messagestext
    global UserColour
    global Select
    username = contents.get()
    if len(str(username)) > 0:
        username = contents.get()
        submitbutton.destroy()
        sendbutton = Button(master, text="Send", command=send)
        sendbutton.place(width=50,height=20,relx = 0.915, rely = 0.975, anchor = CENTER)
        contents.destroy()
        contents = Entry(master)
        contents.place(width=250,height=20, relx = 0.4175, rely = 0.975, anchor = CENTER)
        f = open("SMS.txt", "a")
        f.write(username + " joined the chat" + username + " joined the chat\n")
        f.close()
        f = open("Colour.txt", "a")
        f.write(str(UserColour) + "\n")
        f.close()
        if len(messagestext.split("\n")) > 30:
            messagestext = messagestext.split("\n")
            del messagestext[0]
            messagestext = "\n".join(messagestext)
            f = open("SMS.txt", "a")
            g = f.read()
            g = g.split("\n")
            del g[0]
            g = "\n".join(g)
            f.write(g)
            f.close()
        Select = 1
        master.after(10, refresh)

def refresh():
    global messages
    global messagestext
    global contents
    global StayTyping
    f = open("SMS.txt", "r")
    g = open("Colour.txt", "r")
    messagestext = f.read()
    ColourList = g.read()
    f.close()
    g.close()
    if len(messagestext.split("\n")) > 30:
        messagestext = messagestext.split("\n")
        del messagestext[0]
        messagestext = "\n".join(messagestext)
        f = open("SMS.txt", "w")
        f.write(messagestext)
        f.close()
    messages.destroy()
    d = messagestext.split("\n")
    e = ColourList.split("\n")
    for i in range(0,len(d)-1):
        exec("colour"+str(i) + "= Label(master, text=d[i])")
        eval("colour"+str(i)).place(width=600,height=15, relx = 1, rely = i * (1/29) - 0.035, anchor = E)
        eval("colour"+str(i)).config(background =  e[i])
    #if StayTyping > 0:
    #    StayTyping -= 1
    #else:
        
    master.after(100, refresh)

def typing(event):
    global StayTyping
    StayTyping += 1

messages = Label(master, text="Please input a username")
messages.place(width=600,height=40, relx = 0.5, rely = 0.475, anchor = CENTER)
messages.config(background =  "white")
contents = Entry(master)
contents.place(width=250,height=20, relx = 0.4175, rely = 0.975, anchor = CENTER)
submitbutton = Button(master, text="Submit", command=username)
submitbutton.place(width=50,height=20,relx = 0.915, rely = 0.975, anchor = CENTER)
master.bind('<Return>', enter)
master.bind("<Key>", typing)

mainloop()
