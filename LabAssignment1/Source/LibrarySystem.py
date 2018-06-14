class Person:   #define the class person
    def __init__(self,name,phno): #define the constructor with params as name and phno
        self.name=name #map the name and phonno
        self.phno=phno
    def showDetails(self): #displays the persons name and phoneno

        print("Name:",self.name)
        print("PhoneNo:",self.phno)

class Student(Person):  #define the student class that inherits person class
    studentcount=0   #defines the counter for no of students
    def __init__(self,name,phno,stud_id): ##define constructor with params student id
        super().__init__(name,phno) #calls the super class constructor
        self.stud_id=stud_id #map the student id
        Student.studentcount+=1 #increment the counter

    def showDetails(self): #override showDetails from person class
        print("Student Details:")
        Person.showDetails(self) #displays the student details
        print("Student Id:",self.stud_id)

class Librarian(Person):   #define the library class
    libcount=0
    def __init__(self,name,phno,lib_id): #defines the constructor
        Person.__init__(self,name, phno)  #define the superclass constructor to map name and phone no
        self.lib_id=lib_id #map emp id of librarian
        Librarian.libcount+=1

    def showDetails(self):
        print("Librarian Details:")
        Person.showDetails(self)   #prints the details of librarian
        print("Lib Id:",self.lib_id)

class Book: #defines the book class
    def __init__(self,bookname,author,id):
        self.bookname=bookname
        self.author=author
        self.__id=id

    def showDetails(self):
        print("Book Details:")
        print("Book name:",self.bookname)
        print("Book Author:",self.author)
        print("Book ID:",self.__id)

class LendBook(Student,Book):   #defines the lendbook class

    def __init__(self,name,phno,stud_id,bookname,author,id): #defines the constructor to map bookdetails
        Student.__init__(self,name,phno,stud_id)
        Book.__init__(self,bookname,author,id)


    def showDetails(self):
#displays the details of the book and student
        Student.showDetails(self)
        Book.showDetails(self)

#define the list and append the objects

s1=Student("sharath",12345,16)
l1=Librarian("UMKCLibrary",67890,350)
b1=Book("Python","PythonSE1.6",189045678)
b2=Book("Java","JavaSE",72904789)
lbook1=LendBook("sharath",12345,16,"Python","PythonSE1.6",189045678)
lbook2=LendBook("sharath",12345,16,"Java","JavaSE",72904789)

s1.showDetails()
print("\n")
l1.showDetails()
print("\n")
b1.showDetails()
print("\n")
b2.showDetails()
print("\n")
lbook1.showDetails()
print("\n")
lbook2.showDetails()
print("\n")
print("Total no of students are:",Student.studentcount)
print("Total no of Librarians are:",Librarian.libcount)
