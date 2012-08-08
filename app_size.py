import tkinter

class Application(tkinter.Frame):
    def __init__(self,master):
        tkinter.Frame.__init__(self,master)
        self.config(width=500)
        self.config(height=300)
        self.config(bg="#FF3366")
        self.pack()
        self.CreateWidgets()
    def CreateWidgets(self):
        pass

root=tkinter.Tk()
app=Application(master=root)
app.mainloop()
root.destroy()
