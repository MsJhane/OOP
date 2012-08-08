import tkinter

class Application(tkinter.Frame):
    def __init__(self,master):
        tkinter.Frame.__init__(self,master)
        self.pack()
        self.CreateWidgets()
    def CreateWidgets(self):
        self.label1=tkinter.Label(self)
        self.label1.config(text="Hello world \n I m Jhane. \n Nice to meet you")
        self.label1.config(bg="pink")
        self.label1.config(fg="blue")
        self.label1.pack()
        

root=tkinter.Tk()
app=Application(master=root)
app.mainloop()
root.destroy()
