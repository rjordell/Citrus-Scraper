from canvasapi import Canvas
# Canvas API URL
API_URL = "https://elearn.ucr.edu/"
# Canvas API key (sample, depends on user)
API_KEY = "14493~oYwrW42TOEZOEVBPYV2ZqouIXceIpIHqQARLhgix6Tu1cmksVR7PFuZEEqny9cdG"
# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)
user = canvas.get_user(44909)


# Access the user's name
name = user.name
assignments = user.get_assignments(48816)
print(name)
for assign in assignments:
    print(assign)
