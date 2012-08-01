class Information:
    def SetInfo(self,name,age,schoolyear):
        self.Name=name
        self.Age=age
        self.Schoolyear=schoolyear
    def show(self):
        print("Name: %s " % (self.Name))
        print("Age: %i " % (self.Age))
        print("School Year: %s " % (self.Schoolyear))

class SecondYearInfo(Information):
    def SetInfo(self,name,age):
        self.Name=name
        self.Age=age
        self.Schoolyear="Second"

class ThirdYearInfo(Information):
    def SetInfo(self,name,age):
        self.Name=name
        self.Age=age
        self.Schoolyear="Third"

class FirstYearInfo(Information):
    def SetInfo(self,name,age):
        self.Name=name
        self.Age=age
        self.Schoolyear="First"

        
ListOfStudents=[]
student=SecondYearInfo()
student.SetInfo("Jane",17)
ListOfStudents.append(student)

student=SecondYearInfo()
student.SetInfo("Elvira",22)
ListOfStudents.append(student)

student=SecondYearInfo()
student.SetInfo("Errol",19)
ListOfStudents.append(student)

student=SecondYearInfo()
student.SetInfo("BJ",19)
ListOfStudents.append(student)

student=SecondYearInfo()
student.SetInfo("Joy",19)
ListOfStudents.append(student)

student=ThirdYearInfo()
student.SetInfo("Jamaica",18)
ListOfStudents.append(student)

student=ThirdYearInfo()
student.SetInfo("Ruth",18)
ListOfStudents.append(student)

student=ThirdYearInfo()
student.SetInfo("Noemi",18)
ListOfStudents.append(student)

student=FirstYearInfo()
student.SetInfo("Geraldine",16)
ListOfStudents.append(student)

student=FirstYearInfo()
student.SetInfo("Joanne",16)
ListOfStudents.append(student)

student=FirstYearInfo()
student.SetInfo("Rizza",18)
ListOfStudents.append(student)

for student in ListOfStudents:
    student.show()
