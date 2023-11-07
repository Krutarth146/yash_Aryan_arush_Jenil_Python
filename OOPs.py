# # 50 Students

# class Student
# {
#     int id;
#     char name[30];


    #    Student(name){
            #   this->name = name
    #    }

#     void set_data()
#     {

#     }

#     void display()
#     {

#     }

# };




# struct Library
# {
#     int bookno;
#     char author_name[30];
# };

# void set_book_details()
# {

# }



# void main()
# {
#             int      x;
#     struct Student jenil, aaryan;
# }



# Consturctor -----> TO intialize Member Variable


class Student:
    School = "Ahm Public School"   # Class Variable

    # Variable Types  1. Instance Variable    2. Class Variable
    # Methods  1. Instance   2. Class   3. Static

    def __init__(self,name = None, roll1 = 0) -> None:
        self.name = name   # Instance Varibale
        self.roll = roll1
        print("Student Con. Called")

    def display(self):   # Instance Method
        print(self.name, self.roll)


    @classmethod    # Inbuilt Decorator
    def change_school(cls):
        cls.School = input("Enter School Name: ")
        print("School changed")

    @staticmethod
    def st1():
        print("This is Static Method for faster use")



manoj = Student("Manoj Patel", 67)
keshav = Student()

print(manoj.name)
print(keshav.name)

print(manoj.School)   # Ahm Public School
print(keshav.School)   # Ahm Public School
print(Student.School)

keshav.School = "Royal"   # Modify

print(manoj.School)   # Ahm Public School
print(keshav.School)   # Royal
print(Student.School)  # # Ahm Public School

Student.School = "Technosoft"


print(manoj.School)   # Technosoft
print(keshav.School)   # Royal
print(Student.School)  # Technosoft   # Class Variable


manoj.display()

keshav.change_school()

print(Student.School)
