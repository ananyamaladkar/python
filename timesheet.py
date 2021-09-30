class timesheet:
    def __init__(self, date, noofhours, activity, description, status):
        self.date = date
        self.noofhours = noofhours
        self.activity = activity
        self.description = description
        self.status = status

    def display(self):
            if self.noofhours >40:
                raise Exception("value too large")

t = timesheet("2/5/2021",41, "testing", "idk", "active")
t.display()
