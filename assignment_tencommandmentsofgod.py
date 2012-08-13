import tkinter
import tkinter.font

class Application(tkinter.Frame):
    def __init__(self,master):
        tkinter.Frame.__init__(self,master)
        self.pack()
        self.CreateWidgets()
    def CreateWidgets(self):
        self.label1=tkinter.Label(self)
        self.label1.config(text="The Ten Commandments Of God \n \n Thou shalt have no other gods before me.\n Thou shalt not make unto thee any graven image.\n Thou shalt not take the name of the Lord thy God in vain.\n Remember the sabbath day, to keep it holy.\n Honour thy father and thy mother.\n Thou shalt not kill. \n Thou shalt not commit adultery. \nThou shalt not steal \nThou shalt not bear false witness against thy neighbor.\nThou shalt not covet.")
        self.label1.config(bg="black")
        self.label1.config(fg="violet")
        self.myFont=tkinter.font.Font(family="Chiller",size=26,)
        self.label1.config(font=self.myFont)
        self.label1.pack()
        

root=tkinter.Tk()
app=Application(master=root)
app.mainloop()
root.destroy()
