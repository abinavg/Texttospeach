import tkinter as tk
import pyttsx3
engine = pyttsx3.init()
class Widget():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("TTS")
        self.root.resizable(0,0)
        self.root.configure(background="blue")
        self.label = tk.Label(self.root, bg="blue", fg="yellow", font="Arial 30 bold", text="What you want me to speak?" )
        self.label.pack()
        self.entry = tk.Entry(self.root,width=35, font="arial 25")
        self.entry.pack()
        self.button = tk.Button (self.root, bg="blue", fg="yellow", font="Arial 30 bold", text="SPEAK",command=self.clicked)
        self.button.pack()
        self.root.mainloop()

    def clicked(self):
        text = self.entry.get()
        self.speak(text)

    def speak(self,text):
        engine.say(text)
        engine.runAndWait()
if __name__ == "__main__":
    temp = Widget()