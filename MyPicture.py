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

root=tkinter.Tk()
app=Application(master=root)
app.mainloop()
root.destroy()
