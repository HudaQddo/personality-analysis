import tkinter as tk
import subprocess

rootStart = tk.Tk()

screen_width = rootStart.winfo_screenwidth()
screen_height = rootStart.winfo_screenheight()
canvas = tk.Canvas(rootStart, width=screen_width, height=screen_height, bg='white')
canvas.grid(columnspan=3, rowspan=6)

logo = tk.Label(rootStart, text="Personal Analysis", font=("Segoe Print", 25),bg='white' ,fg="#006E7F")
logo.grid(column = 1, row = 0)

startButton = tk.Button(rootStart, text="Start", command=lambda *args: clickStart(), font=("Consolas",15), bg="#2F8F9D", fg="white", height=2, width=15)
startButton.grid(column = 1, row = 2)

languageButton = tk.Button(rootStart, text="EN", command=lambda *args: swapLanguage(), font=("Consolas",12), bg="white", fg="black", width=12)
languageButton.grid(column = 1, row = 4)

def swapLanguage():
    if languageButton['text'] == "EN":
        languageButton['text'] = "AR"
    else:
        languageButton['text'] = "EN"

def clickStart():
    f = open("language.txt", "w")
    f.write(languageButton['text'])
    f.close()
    
    subprocess.call(["python", "main.py"])
    rootStart.destroy()
    return

rootStart.mainloop()