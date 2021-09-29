
class employee:
    def __init__ (self,empid,empname,empdept):
        self.empid=empid
        self.empname=empname
        self.empdept=empdept
    def display(self):
        print(self.empid,
        self.empname,
        self.empdept)


e=employee("20810", "BHUVAN", "ANALYST",)
e.display()