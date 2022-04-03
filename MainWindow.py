
from tkinter import *
import string
from icalendar import Calendar
from datetime import date, timedelta
from  send_sm import *
#-----------------------
acc_sid = 'AC4f786eff34248408e94260ba0cbbf97d'
token = 'e9b981f2ac30c03817e1318623143331'
#------------------------
#text = "Due date: April 7, 2022 Assignment: Hw1"

#send_text(acc_sid, token, text)
#-------------------------

today = date.today() + timedelta(days = 5)

print(today)

# file = open('test.ics', 'rb')
file = open('/Users/victorsandoval/canvas calender assignment/CitrusScraper/test.ics')
cal = Calendar.from_ical(file.read())
for component in cal.walk():
    if component.name == "VEVENT":
        print(component.get('SUMMARY'))
        dDate = component.decoded('DTEND')
        sep = ' '
        #ddDate = dDate.split(sep, 1)[0]
        print(dDate)
        #if dDate < today:
          #  text = component.get('SUMMARY') + dDate
           # send_text(acc_sid, token, text)



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
