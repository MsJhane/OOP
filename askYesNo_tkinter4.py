import tkinter

class Application(tkinter.Frame):
    def __init__(self,master):
        tkinter.Frame.__init__(self,master)
        self.pack()
        self.points = 0

        self.question1button=tkinter.Button()
        self.question1button["text"]="Question1"
        self.question1button["command"]=self.question1
        self.question1button.pack()

        self.question2button=tkinter.Button()
        self.question2button["text"]="Question2"
        self.question2button["command"]=self.question2
        self.question2button.pack()

        self.question3button=tkinter.Button()
        self.question3button["text"]="Question3"
        self.question3button["command"]=self.question3
        self.question3button.pack()

        self.pointsbutton=tkinter.Button()
        self.pointsbutton["text"]="Points"
        self.pointsbutton["command"]=self.DisplayPoints
        self.pointsbutton.pack()
    
    
        self.quitbutton=tkinter.Button()
        self.quitbutton["text"]="Quit"
        self.quitbutton["command"]=self.exit
        self.quitbutton.pack()

    def question1(self):
            response=tkinter.messagebox.askyesno("Question #1","Is the sun yellow?")
            if (response==True):
                self.points+=1
                            

    def question2(self):
            response=tkinter.messagebox.askyesno("Question #2","Is wood edible?")
            if (response==True):
               self.points+=1

    def question3(self):
           response=tkinter.messagebox.askyesno("Question #3","I fried chicken made of pigs?")
           if (response==True):
               self.points+=1

    def DisplayPoints(self):
           tkinter.messagebox.showinfo("Points","Your points are: %i " % (self.points))
           
    def exit(self):
            response=tkinter.messagebox.askyesno("Bye bye?","Do you want to quit!")
            if (response==True):
                self.quit()
        

root=tkinter.Tk()
app=Application(master=root)
app.mainloop()
root.destroy()

