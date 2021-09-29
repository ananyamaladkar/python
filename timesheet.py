class timesheet:
    def __init__ (self, date, noofhrs, activity, description, status):
        self.date = date
        self.noofhrs = noofhrs
        self.activity = activity
        self.description = description
        self.status= status

    def display(self):
        print(self.noofhrs)

t = timesheet("2/5/2021", "8hrs", "testing", "idk", "active")
t.display()
