# CitrusScraper
A program that signs a user up for text alerts based on events from their calendar.

Made by Bilal Nasir, Jordell Rodrigues, Braxton Mott, and Victor Sandoval Vargas. 


# Overview
This program is written in python and the most of the logic is incorporated in the file 
```
MainWindow.py
```
When ran, the program will open a window with three buttons, one to manually add assignments, one to sync their google calendar, and one to sign up for text alerts.
Upon clicking the one to manually add assignments, they are prompted to give the assignment name, due date, and due time. 

As of 04/03/2022, we couldn't complete the syncing google calendar functionality, however we are close. We can succesfully read and sort through an icalendar or "ics" file. Moving forward, we would need to find a way to use python and the google calendar api to get access to the users ics file. From there our logic should work in reading through the file. 

Finally, when running the "sign up for text messages button", the user is prompted to enter their phone number. This phone number is used as the "send" recipient for twilio and the logic for sending messages is under the file 
```
send_sm.py
```
We send a message of all the assignments due in the future along with their due datees straight to the users inputted phone number. Moving forward we would like to have this gap closed to "all assignments due this week" and "all assignments due today". This was possible however we had a limitation of not having a server to continually run the program. Additionally, we would also need a full access twilio account as eventually our free trial will end. 

