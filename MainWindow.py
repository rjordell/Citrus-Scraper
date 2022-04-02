from tkinter import *
import string

global allAssignments

allAssignments  = []

window=Tk()

#set geometry and title of main window
window.title('Course Scheduler')
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
        #dueDate.translate(None, string.letters)
        dueDate = dueDate.translate(dueDate.maketrans("", "", string.ascii_letters))
        manualWindow.destroy()
        assignmentInfo = [name, dueDate]
        print("added ", assignmentInfo)
        allAssignments.append(assignmentInfo)


    btn = Button(manualWindow, text="Add Assignment", command = getInput).grid(row = 5, sticky = W)




# add widgets here
btn = Button(window, text="Manually Add Assignment", fg="black", command=openManualWindow)
btn.place(x=50, y=100)

btn = Button(window, text="Sign in with Canvas", fg="black")
btn.place(x=300, y=100)

btn = Button(window, text="Generate Calendar", fg='black', command = generateCalendar)
btn.place(x=200, y=250)

window.mainloop()
