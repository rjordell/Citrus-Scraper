from tkinter import *
import string
from icalendar import Calendar
from datetime import date

file = open('test.ics', 'rb')
cal = Calendar.from_ical(file.read())
for component in cal.walk():
    if component.name == "VEVENT":
        print(component.get('SUMMARY'))
        dDate = component.decoded('DTEND')
        print(dDate)



file.close()

global allAssignments
allAssignments  = []

window=Tk()

#set geometry and title of main window
window.title('Assignment Scheduler')
window.geometry("500x400")




#define functions of buttons
def generateCalendar():
    global allAssignments

    allAssignments.sort(key = lambda x: int(x[1]))
    print(allAssignments)

def openManualWindow():
    manualWindow = Toplevel(window)
    manualWindow.title("Manual Assignment Insertion")
    manualWindow.geometry("500x400")

    lbl=Label(manualWindow, text="Assignment Name").grid(row = 1, sticky = W)
    AName=Entry(manualWindow)

    lbl=Label(manualWindow, text="Assignment Due Date (mm/dd/year)").grid(row = 3, sticky = W)
    ADueDate=Entry(manualWindow)

    AName.grid(row = 1, column = 1)
    ADueDate.grid(row = 3, column = 1)

    def getInput():
        global allAssignments
        name=AName.get()
        dueDate=ADueDate.get()
        dueDate = dueDate.translate(dueDate.maketrans("", "", string.ascii_letters))
        #manualWindow.destroy()
        AName.delete(0, END)
        ADueDate.delete(0, END)
        assignmentInfo = [name, dueDate]
        print("added ", assignmentInfo)
        allAssignments.append(assignmentInfo)
    def backButton():
        manualWindow.destroy()

    btn = Button(manualWindow, text="Add Assignment", command = getInput).grid(row = 5, column = 0, sticky = W)
    btn = Button(manualWindow, text ="Go Back", command = backButton).grid(row = 5, column = 1, sticky = W)



# add widgets here
btn = Button(window, text="Add Assignments", fg="black", command=openManualWindow)
btn.place(x=50, y = 50)

btn = Button(window, text="Sign in with Canvas", fg="black")
btn.place(x=50, y= 80)

btn = Button(window, text="Generate Calendar", fg='black', command = generateCalendar)
btn.place(x=50, y=350)

window.mainloop()
