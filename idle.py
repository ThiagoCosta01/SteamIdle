import os
import time
from tkinter import *

#Window configs
root = Tk()
root.title("Steam Idle")
root.geometry("500x570+800+150")
root.resizable(1,1)
root.config(bg="#012940")

#Functions
fileName = "D:\Steam\steamapps\common\Transformice\Steam_appid.txt"

def getID():
    try:
        id = appEntry.get()
    except:
        print("erro no GAME id")
    else:
        os.system('cmd /c "taskkill /IM transformice.exe /f /t"')
        rewriteID(id)
        return id

def rewriteID(id):
    if (id):
        with open(fileName, 'w') as file:
            file.write(id)
            file.close()
            time.sleep(1)
            os.system('cmd /c "D:\Steam\steamapps\common\Transformice\Transformice.exe"')

def showID():
    with open(fileName, 'r') as file:
        contents = file.readlines()
    return contents

#Main
id = showID()

idling = Label(root, text="Now Idling:", bg="#C4252A")
idling.grid(column=1, row=1)

appEntry = Entry(root)
appEntry.grid(column=2, row=1)
appEntry.insert(0,id)

botao = Button(root, width=1, height=1, command=getID)
botao.grid(column=3, row=1)



root.mainloop()
