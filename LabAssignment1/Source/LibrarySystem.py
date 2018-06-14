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
        print("Lib Id:")

class Book(Student):   #defines the book class

    def __init__(self,name,phno,stud_id,bookname,author,id): #defines the constructor to map bookdetails
        Student.__init__(self,name,phno,stud_id)
        self.bookname=bookname
        self.author=author
        self._id=id

    def showDetails(self):
#displays the details of the book
        Student.showDetails(self)
        print("Bookname:",self.bookname)
        print("Author:",self.author)
        print("Lib ID:",self._id)

#define the list and append the objects
objlist=[]
buk=Book("sharath",12345,16,"Java","JavaSE",72904789)
objlist.append((Student("sharath",12345,16)))
objlist.append(Librarian("UMKCLibrary",67890,350))
objlist.append(Book("sharath",12345,16,"Python","PythonSE1.6",189045678))

#iterate the objects in the list and prints the details and student count
for ob,list in enumerate(objlist):
    list.showDetails()
    print("\n")
buk.showDetails()
print("\n")
print("Total no of students are:",Student.studentcount)
print("Total no of Librarians are:",Librarian.libcount)
