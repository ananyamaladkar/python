class employee:
    def __init__ (self, empid, empname, empsal, empdept):
        self.empid= empid
        self.empname = empname
        self.empsal = empsal
        self.empdept= empdept

    def display(self):
       print(self.empname)

e = employee ("427","ananya","5000", "hr")
e.display()
