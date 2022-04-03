from canvasapi import Canvas

# Canvas API URL
API_URL = "https://elearn.ucr.edu/"
# Canvas API key (sample, depends on user)
API_KEY = "14493~ErBhp4kBc5bjw21D9N7yQCFh7BC6yB4hR5CSoI6O0qnZfAcwTAyxveq6AWC2rLKc"

def __getitem__(self, i):
    return f"Value {i}"

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)
user = canvas.get_user(38212)
# Access the user's name
name = user.name
course = user.get_courses();
assignments = user.get_assignments(48816)
print(name)
for assign in assignments:
    print(assign["due_at"])

dates = user.get_calendar_events_for_user();

print(dates)

