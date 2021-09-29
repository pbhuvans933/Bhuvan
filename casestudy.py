class employee:
    def __init__ (self,empid,empname,empdept):
        self.empid=empid
        self.empname=empname
        self.empdept=empdept
    def display(self):
        print(self.empid,
        self.empname,
        self.empdept)


class timesheet(employee):
    def __init__(self, date, noofhrs, activity, description, status):
        self.date = date
        self.noofhrs = noofhrs
        self.activity = activity
        self.description = description
        self.status = status

    def display(self):
        print(self.date,self.noofhrs,self.activity, self.description, self.status)
e=employee("20870","Bhuvan","ANALYST")
e.display()
t=timesheet("29-09-2021", "8hrs", "Training","Python Training","active")
t.display()