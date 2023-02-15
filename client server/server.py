# first import socket,threading,tkinter  
import threading as th
import socket as s
import tkinter as tk
#send function
def send():
    vall = val.get()
    c.send(str(vall).encode())
    s = 4
    tk.Label(window,text="server {}".format(vall),bg="white",fg="black",font=("Tahoma",15)).grid(row=s,column=0)
    s+=1
#get value from client function
def getv():
    data = c.recv(1024)
    s = 4
    tk.Label(window,text="client {}".format(data.decode()),bg="white",fg="black",font=("Tahoma",15)).grid(row=s,column=0)
    s+=1
#create gui
window = tk.Tk()
val = tk.StringVar()
window.geometry("400x400")
window.title("higap")
window.config(bg="black")
#_______________________________________________
#create connection 
server = s.socket(s.AF_INET,s.SOCK_STREAM)
#bind localhost
server.bind(("localhost",8000))
#The number of people who can connect to the server
server.listen(2)
# address of clients and connection of them 
c,addr = server.accept()
#gui
tk.Label(window,text="wellcome to higap",bg="black",fg="white",font=("Tahoma",15)).grid(row=1,column=0)
tk.Label(window,text="Enter your text here",bg="black",fg="white",font=("Tahoma",15)).grid(row=2,column=0)
tk.Entry(window,textvariable=val,bg="black",fg="white",font=("Tahoma",15),bd=0).grid(row=3,column=0)
tk.Button(window,text="send",bg="black",fg="white",font=("Tahoma",15),bd=0,command=(send)).grid(row=3,column=1)
t = th.Thread(target=getv)
t.start()
window.mainloop()
