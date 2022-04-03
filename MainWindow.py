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


def textMessageAlerts():
    smsWindow = Toplevel(window)
    smsWindow.title("Sign up for SMS alerts")
    smsWindow.geometry("500x400")

    Label(smsWindow, text = "Enter Phone Number: ").place(x=50, y = 50)
    phoneNumber=Entry(smsWindow)
    phoneNumber.place(x=50, y= 80)


    def addPhone():
        number = phoneNumber.get()
        phoneNumber.delete(0, END)
    def closeSMS():
        smsWindow.destroy()

    Button(smsWindow, text="Add Phone Number", command = addPhone).place(x = 50, y = 250)
    Button(smsWindow, text ="Back", command = closeSMS).place(x = 50, y = 280)

def openManualWindow():
    manualWindow = Toplevel(window)
    manualWindow.title("Manual Assignment Insertion")
    manualWindow.geometry("500x400")

    Label(manualWindow, text="Assignment Name").grid(row = 1, sticky = W)
    AName=Entry(manualWindow)

    Label(manualWindow, text="Assignment Due Date (mm/dd/year)").grid(row = 3, sticky = W)
    ADueDate=Entry(manualWindow)

    AName.grid(row = 1, column = 1)
    ADueDate.grid(row = 3, column = 1)

    def getInput():
        global allAssignments
        name=AName.get()
        dueDate=ADueDate.get()
        dueDate = dueDate.translate(dueDate.maketrans("", "", string.ascii_letters))
        AName.delete(0, END)
        ADueDate.delete(0, END)
        assignmentInfo = [name, dueDate]
        print("added ", assignmentInfo)
        allAssignments.append(assignmentInfo)

    def closeManual():
        manualWindow.destroy()

    Button(manualWindow, text="Add Assignment", command = getInput).grid(row = 5, column = 0, sticky = W)
    Button(manualWindow, text ="Go Back", command = closeManual).grid(row = 5, column = 1, sticky = W)



# add widgets here
Button(window, text="Add Assignments", fg="black", command=openManualWindow).place(x=50, y = 50)
Button(window, text="Sync Google Calendar", fg="black").place(x=50, y= 80)
Button(window, text="Sign up for text message alerts", fg='black', command = textMessageAlerts).place(x=50, y=350)

window.mainloop()
