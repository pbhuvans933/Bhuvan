class timesheet:
    def __init__ (self, date, noofhrs, activity, description, status):
        self.date = date
        self.noofhrs =  noofhrs
        self.activity = activity
        self.description = description
        self.status = status

    def display(self):
        print(self.status,self.date,self.noofhrs,self.description,self.status)


t = timesheet("2/5/2021", "8hrs", "DEVELOPER","idk","active")
t.display()

