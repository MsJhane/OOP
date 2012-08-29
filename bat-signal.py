import tkinter

class Application(tkinter.Frame):
    def __init__(self,master):
        tkinter.Frame.__init__(self,master)
        self.pack()
        self.CreateWidgets()
    def CreateWidgets(self):
        self.image=tkinter.PhotoImage(file="jhane.gif")
        self.label1=tkinter.Label(image=self.image)
        self.label1.pack()
        self.image2=tkinter.PhotoImage(file="bat-signal.gif")
        self.button1=tkinter.Button(image=self.image2)
        self.button1["command"]=self.batsignal
        self.button1.pack()
    def batsignal(self):
        tkinter.messagebox.showinfo("BATMAN","PARATING NA SI BATTMAN!")
root=tkinter.Tk()
app=Application(master=root)
app.mainloop()
root.destroy()

