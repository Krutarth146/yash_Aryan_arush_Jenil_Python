import mysql.connector
import Jenil_Project

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='5685',
    database='gyms'
)

# Function to add a new member
def add_member():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    name = input("Enter member name: ")
    age = int(input("Enter member age: "))
    email = input("Enter member email: ")
    height = int(float(input("enter your height in metres: ")))
    weight = int(float(input("enter your weight in kg: ")))

    bmi = int(weight/ height ** 2)
    print("Your Body Mass Index is: ",bmi)
    print("Member added successfully.")
    return username, password, name, age, email, height, weight, bmi
    



def primary_prog(bmi):
    print("You are Underweight.")
    print("You should include following items in your diet:")
    print("1 - Whole Milk")
    print("2 - Plenty of protein supplements")
    print("3 - Carbohydrates")
    print("4 - Cheese and other dairy products")
    print("You will also have to burn minimum 50 percentage of the total calorie intake.")
    list1 = ["You are Underweight."]
    return list1



def secondary_prog(bmi):
    print("Your BMI is normal.")
    print("You should include following items in your diet:")
    print("1 - Whole Milk")
    print("2 - Adequate of protein supplements")
    print("3 - Carbohydrates")
    print("You will also have to maintain your current calorie intake ratio and calorie burn ratio.")
            

def third_prog(bmi):
    if bmi>=25.0 and bmi<=29.9:
            print("You are Overweight.")
            print("You should include following items in your diet:")
            print("1 - Milk with least fats")
            print("2 - Plenty of fibre rich supplements")
            print("3 - Fruits with good amount of fibre and water content")
            print("4 - Instead of wheat and rice have bajra and oats")
            print("You will also have to burn minimum 80 percentage of the total calorie intake.")
        
def fourth_prog(bmi):
    if bmi>=30.0 and bmi<=34.9:
            print("You are in Obesity Class 1.")
            print("You should include following items in your diet:")
            print("1 - Milk with least fats")
            print("2 - Plenty of fibre rich supplements")
            print("3 - Fruits with good amount of fibre and water content")
            print("4 - Instead of wheat and rice have bajra and oats")
            print("You will also have to burn minimum 90 percentage of the total calorie intake.")
        
def fifth_prog(bmi):
    if bmi>=35.0 and bmi<=39.9:
            print("You are in Obesity Class 2.")
            print("You should include following items in your diet:")
            print("1 - Milk with least fats")
            print("2 - Plenty of fibre rich supplements")
            print("3 - Fruits with good amount of fibre and water content")
            print("4 - Instead of wheat and rice have bajra and oats")
            print("You will also have to burn minimum 100 percentage of the total calorie intake.")
            print("Also if consult a doctor if required.")

def six_prog(bmi):
    if bmi>=40.0 and bmi<=49.9:
            print("You are in Obesity Class 3.")
            print("Consult a doctor at the earliest.")



# Function to view member details
def view_member(username, password):

    if username == username and password == password:
        pass
    member_id = int(input("Enter member ID: "))
    
    # Prepare the SQL statement
    sql = "SELECT * FROM members WHERE id = %s"
    
    # Prepare the data for the SQL statement
    data = (member_id,)
    
    # Execute the SQL statement
    cursor = connection.cursor()
    cursor.execute(sql, data)
    result = cursor.fetchone()
    
    # Display member details
    if result:
        print("Member ID:", result[3])
        print("Name:", result[1])
        print("Age:", result[2])
        print("Email:", result[3])
    else:
        print("Member not found.")


def store(username, password, name, age, email, height, weight, bmi):


    if bmi < 18.5:
        comment = primary_prog(bmi)
    elif bmi>=18.5 and bmi<=24.9:
        comment = secondary_prog(bmi)
              
    # Prepare the SQL statement
    # id INT AUTO_INCREMENT PRIMARY KEY,
    # name varchar(255),

    sql = "INSERT INTO members (username, password, name, age, email, height, weight, bmi, comment) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    # Jenil_Project.bmi()
    # Prepare the data to be inserted
    data = (username, password, name, age, email, height, weight, bmi, comment)
    
    # Execute the SQL statement
    cursor = connection.cursor()
    cursor.execute(sql, data)
    connection.commit()

def modify():
    member_id = int(input("Enter member ID: "))
    
    # Prepare the SQL statement
    sql = "SELECT * FROM members WHERE id = %s"
    
    # Prepare the data for the SQL statement
    data = (member_id,)
    
    # Execute the SQL statement
    cursor = connection.cursor()
    cursor.execute(sql, data)
    result = cursor.fetchone()

    print(result)

# Main menu
while True:
    print("----- Gym Management System -----")
    username = input("ENter Username: ")
    password = input("ENter Password: ")
    print("1. Add Member")
    print("2. View Member Details")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
        r_data = add_member()   # BMI stored
        store(r_data)
    elif choice == '2':
        view_member(username, password)
    elif choice == '3':
        break
    elif choice == '4':
        modify()
    else:
        print("Invalid choice. Please try again.")



# Close the database connection
connection.close()
