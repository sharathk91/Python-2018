class Employee: #define the employee class

    #initialize the empcount,totalsaland avgsal to 0
    empcount=0
    totalsal=0
    avgsal=0

    #define constructor and map the values
    def __init__(self,name,family,sal,dept): #constructor
        self.name = name
        self.family =  family
        self.salary = sal
        self.department = dept
        Employee.empcount+=1
        Employee.totalsal+=sal

   #define the logic for computing avgsalary
    def avgsalary(self):   #public method
        avgsal=Employee.totalsal/Employee.empcount
        print("Average Salary of Employees:",avgsal)

   #cmpute employee count
    def calcemployees(self):    #public method
        print("Total Employees are:",Employee.empcount)

   #prints the employee details
    def displayDetails(self):   #public method
        print("Name:",self.name,"Family:",self.family,"Salary:",self.salary,"Department:",self.department)

#define fulltime class which is extending parent class employee
class FullTimeEmployee(Employee):   #single inheritance
    #define constructor and call parent class constructor
    def __init__(self,n,f,s,d):     #child class constructor
        Employee.__init__(self,n,f,s,d)

#define the objects for base & super class
e1=Employee("sharath","A",3000,"D1")
e2=Employee("Rohith","B",4000,"D2")
fe1=FullTimeEmployee("krishna","C",5000,"D3")
fe2=FullTimeEmployee("Rahul","D",6000,"D4")

#call the methods in base class
e1.displayDetails()
e2.displayDetails()
fe1.displayDetails()
fe2.displayDetails()

#cal to compute avgsal and empcount and print it
fe2.avgsalary()
fe2.calcemployees()




