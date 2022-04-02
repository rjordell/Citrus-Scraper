from tkinter import *
window=Tk()

#set geometry and title of main window
window.title('Course Scheduler')
window.geometry("500x400")

#define functions of buttons
def openManualWindow():
    manualWindow = Toplevel(window)
    manualWindow.title("Manual Assignment Insertion")
    manualWindow.geometry("500x400")

    lbl=Label(manualWindow, text="Assignment Name")
    lbl.place(x=60, y=50)
    txtfld=Entry(manualWindow, bd=5)
    txtfld.place(x=60, y=80)

    btn = Button(manualWindow, text="Add Assignment")
    btn.place(x=50, y=400)





# add widgets here
btn = Button(window, text="Manual Assignment Insertion", fg="black", command=openManualWindow)
btn.place(x=50, y=100)

btn = Button(window, text="Sign in with Canvas", fg="black")
btn.place(x=300, y=100)

btn = Button(window, text="View Calendar", fg='black')
btn.place(x=200, y=250)

window.mainloop()
