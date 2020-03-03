import tkinter as tk
from googletrans import Translator

def Trans():
    word = entry.get()
    translator = Translator(service_urls=["translate.google.com"])
    translation = translator.translate(word,dest='fr')
    label1 = tk.Label(win,text=f'Translated word : {translation.text}',bg="yellow")
    label1.grid(row=2,column=1)


win = tk.Tk()
win.title("Translator BY VikasMalviy")
# win.config(height=500,width=500)
win.geometry("400x400")
label = tk.Label(win,text="Write here : ")
label.grid(row=1,column=2)
entry = tk.Entry(win)
entry.grid(row=1,column=2)
button = tk.Button(win,text="Translate",command=Trans)
button.grid(row=3,column=2)

win.mainloop()