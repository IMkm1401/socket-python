# first import socket,threading,tkinter  
import socket
import threading
import tkinter as tk
#create connection with socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#_________________________________________________________________________
#your ip
ip = "localhost"
#your port
port = 8000
#connect to your server with ip address and port
client.connect((ip,port))
#send function
def sendval():
    s = 4
    message = val.get()
    # we send data with send() method in socket programming
    client.send(message.encode())
    tk.Label(window,text="client {}".format(message),bg="white",fg="black",font=("Tahoma",15)).grid(row=s,column=0)
    s+=1
#get data from server function
def getval():
    s = 4
    # we get data with recv method in socket programming
    data = client.recv(1024)
    tk.Label(window,text="server {}".format(data.decode()),bg="white",fg="black",font=("Tahoma",15)).grid(row=s,column=0)
    s+=1
# create gui
window = tk.Tk()
val = tk.StringVar()
window.geometry("400x400")
window.title("higap")
window.config(bg="black")
if window.quit():
    client.close()
tk.Label(window,text="wellcome to higap",bg="black",fg="white",font=("Tahoma",15)).grid(row=1,column=0)
tk.Label(window,text="Enter your text here",bg="black",fg="white",font=("Tahoma",15)).grid(row=2,column=0)
tk.Entry(window,textvariable=val,bg="black",fg="white",font=("Tahoma",15),bd=0).grid(row=3,column=0)
tk.Button(window,text="send",bg="black",fg="white",font=("Tahoma",15),bd=0,command=(sendval)).grid(row=3,column=1)

#threading
t = threading.Thread(target=getval)
t.start()
window.mainloop()
