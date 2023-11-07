import mysql.connector
# import Jenil_Project
# import uname_pass
# import login_user
# import __u
# from __u import register_user
# Establish a connection to the MySQL database
a=mysql.connector.connect(user="root",passwd="5685",host="localhost",database="gym")
    
cursor=a.cursor()
def register_user():
    username = input("Enter your username: ")
    password = input("Enter your password (8 characters): ")
    
    if len(password) != 8:
        print("Password should be 8 characters long.")
        return
    
    u_id = input("Enter your unique ID: ")
    
    # Check if the ID is already taken
    cursor.execute("SELECT id FROM credentials WHERE id = %s", (u_id,))
    if cursor.fetchone():
        print("ID is already taken. Please choose a different one.")
    else:
        # Check if the username is already taken
        cursor.execute("SELECT id FROM credentials WHERE username = %s", (username,))
        if cursor.fetchone():
            print("Username is already taken. Please choose a different one.")
        else:
            sql = "INSERT INTO credentials (id, username, password) VALUES (%s, %s, %s)"
            values = (u_id, username, password)
            cursor.execute(sql, values)
            name = input("Enter member name: ")
            age = int(input("Enter member age: "))
            gender = input("Enter your gender: ")
            email = input("Enter member email: ")
            height = float(input("enter your height in metres: "))

            weight = int(input("enter your weight in kg: "))
            h_b=height ** 2
            bmi = weight/h_b #20
            print("Your Body Mass Index is: ",bmi)
            f_1_u=first_program()
            f_2_u=second_program()
            f_3_u=third_program()
            f_4_u=fourth_program()
            f_5_u=fifth_program()
            f_6_u=sixth_program()
            if bmi<18.5:
                first_program()
                sql_1= ("INSERT INTO members(m_id,name,gender,age,email,height,weight,bmi,diet) VALUES('{}','{}','{}','{}','{}',' {}','{}','{}')").format(u_id,name,gender,age,email,height,weight,bmi,)
                try:
                    cursor.execute(sql_1,)
                    # sql_v=("SELECT * FROM CREDENTIALS WHERE ID={}".format())    
                    # cursor.execute(sql_v,)
                    a.commit()
                    print("Member added successfully.")
                except Exception as e:
                    print("Error:",e)
                    print("Please enter any other username.")
                    # pass
            elif bmi>=18.5 and bmi<24.9:
                second_program()
                sql_2= ("INSERT INTO members(m_id,name,gender,age,email,height,weight,bmi,diet) VALUES('{}','{}','{}','{}','{}',' {}','{}','{}')").format(u_id,name,gender,age,email,height,weight,bmi,)
                try:
                    cursor.execute(sql_2,)
                    # sql_v=("SELECT * FROM CREDENTIALS WHERE ID={}".format())    
                    # cursor.execute(sql_v,)
                    a.commit()
                    print("Member added successfully.")
                except Exception as e:
                    print("Error:",e)
                    # print("Please enter any other username.")
                    # pass
            elif bmi>=24.9 and bmi<29.9:
                third_program()
                sql_3= ("INSERT INTO members(m_id,name,gender,age,email,height,weight,bmi,diet) VALUES('{}','{}','{}','{}','{}',' {}','{}','{}')").format(u_id,name,gender,age,email,height,weight,bmi,)
                try:
                    cursor.execute(sql_3,)
                    # sql_v=("SELECT * FROM CREDENTIALS WHERE ID={}".format())    
                    # cursor.execute(sql_v,)
                    a.commit()
                    print("Member added successfully.")
                except Exception as e:
                    print("Error:",e)
                    # print("Please enter any other username.")
                    # pass
            elif bmi>=29.9 and bmi<34.9:
                fourth_program()
                sql_4= ("INSERT INTO members(m_id,name,gender,age,email,height,weight,bmi,diet) VALUES('{}','{}','{}','{}','{}',' {}','{}','{}')").format(u_id,name,gender,age,email,height,weight,bmi,)
                try:
                    cursor.execute(sql_4,)
                    # sql_v=("SELECT * FROM CREDENTIALS WHERE ID={}".format())    
                    # cursor.execute(sql_v,)
                    a.commit()
                    print("Member added successfully.")
                except Exception as e:
                    print("Error:",e)
                    # print("Please enter any other username.")
                    # pass
            elif bmi>=34.9 and bmi<39.9:
                fifth_program()
                sql_5= ("INSERT INTO members(m_id,name,gender,age,email,height,weight,bmi,diet) VALUES('{}','{}','{}','{}','{}',' {}','{}','{}')").format(u_id,name,gender,age,email,height,weight,bmi,)
                try:
                    cursor.execute(sql_5,)
                    # sql_v=("SELECT * FROM CREDENTIALS WHERE ID={}".format())    
                    # cursor.execute(sql_v,)
                    a.commit()
                    print("Member added successfully.")
                except Exception as e:
                    print("Error:",e)
                    # print("Please enter any other username.")
            # pass
            elif bmi>=39.9 and bmi<49.9:
                sixth_program()
                sql_6= ("INSERT INTO members(m_id,name,gender,age,email,height,weight,bmi,diet) VALUES('{}','{}','{}','{}','{}',' {}','{}','{}')").format(u_id,name,gender,age,email,height,weight,bmi,)
                try:
                    cursor.execute(sql_6,)
                    # sql_v=("SELECT * FROM CREDENTIALS WHERE ID={}".format())    
                    # cursor.execute(sql_v,)
                    a.commit()
                    print("Member added successfully.")
                except Exception as e:
                    print("Error:",e)
                    # print("Please enter any other username.")
                    a.commit()
                    print("User registered successfully!")
    return u_id
# Function to add a new member
def add_member():
    u_id=register_user()
    # user = input("Please create your username: ")
    # pass1 = int(input("Please create a password of 8 digit: "))
    # username = input("Enter Username: ")
    # password = input("Enter Password: ")
    # u_id=uname_pass.credentials()
    name = input("Enter member name: ")
    age = int(input("Enter member age: "))
    gender = input("Enter your gender: ")
    email = input("Enter member email: ")
    height = float(input("enter your height in metres: "))

    weight = int(input("enter your weight in kg: "))
    h_b=height ** 2
    bmi = weight/h_b #20
    print("Your Body Mass Index is: ",bmi)
    f_1_u=first_program()
    f_2_u=second_program()
    f_3_u=third_program()
    f_4_u=fourth_program()
    f_5_u=fifth_program()
    f_6_u=sixth_program()
    if bmi<18.5:
        f1=first_program()
        sql_1= ("INSERT INTO members(m_id,name,gender,age,email,height,weight,bmi,diet) VALUES('{}','{}','{}','{}','{}',' {}','{}','{}')").format(u_id,name,gender,age,email,height,weight,bmi,f1)
        try:
            cursor.execute(sql_1,)
            # sql_v=("SELECT * FROM CREDENTIALS WHERE ID={}".format())    
            # cursor.execute(sql_v,)
            a.commit()
            print("Member added successfully.")
        except Exception as e:
            print("Error:",e)
            print("Please enter any other username.")
            # pass
    elif bmi>=18.5 and bmi<24.9:
        f2=second_program()
        sql_2= ("INSERT INTO members(m_id,name,gender,age,email,height,weight,bmi,diet) VALUES('{}','{}','{}','{}','{}',' {}','{}','{}')").format(u_id,name,gender,age,email,height,weight,bmi,f2)
        try:
            cursor.execute(sql_2,)
            # sql_v=("SELECT * FROM CREDENTIALS WHERE ID={}".format())    
            # cursor.execute(sql_v,)
            a.commit()
            print("Member added successfully.")
        except Exception as e:
            print("Error:",e)
            print("Please enter any other username.")
            # pass
    elif bmi>=24.9 and bmi<29.9:
        f3=third_program()
        sql_3= ("INSERT INTO members(m_id,name,gender,age,email,height,weight,bmi,diet) VALUES('{}','{}','{}','{}','{}',' {}','{}','{}')").format(u_id,name,gender,age,email,height,weight,bmi,f3)
        try:
            cursor.execute(sql_3,)
            # sql_v=("SELECT * FROM CREDENTIALS WHERE ID={}".format())    
            # cursor.execute(sql_v,)
            a.commit()
            print("Member added successfully.")
        except Exception as e:
            print("Error:",e)
            print("Please enter any other username.")
            # pass
    elif bmi>=29.9 and bmi<34.9:
        f4=fourth_program()
        sql_4= ("INSERT INTO members(m_id,name,gender,age,email,height,weight,bmi,diet) VALUES('{}','{}','{}','{}','{}',' {}','{}','{}')").format(u_id,name,gender,age,email,height,weight,bmi,f4)
        try:
            cursor.execute(sql_4,)
            # sql_v=("SELECT * FROM CREDENTIALS WHERE ID={}".format())    
            # cursor.execute(sql_v,)
            a.commit()
            print("Member added successfully.")
        except Exception as e:
            print("Error:",e)
            print("Please enter any other username.")
            # pass
    elif bmi>=34.9 and bmi<39.9:
        f5=fifth_program()
        sql_5= ("INSERT INTO members(m_id,name,gender,age,email,height,weight,bmi,diet) VALUES('{}','{}','{}','{}','{}',' {}','{}','{}')").format(u_id,name,gender,age,email,height,weight,bmi,f5)
        try:
            cursor.execute(sql_5,)
            # sql_v=("SELECT * FROM CREDENTIALS WHERE ID={}".format())    
            # cursor.execute(sql_v,)
            a.commit()
            print("Member added successfully.")
        except Exception as e:
            print("Error:",e)
            print("Please enter any other username.")
            # pass
    elif bmi>=39.9 and bmi<49.9:
        f6=sixth_program()
        sql_6= ("INSERT INTO members(m_id,name,gender,age,email,height,weight,bmi,diet) VALUES('{}','{}','{}','{}','{}',' {}','{}','{}')").format(u_id,name,gender,age,email,height,weight,bmi,f6)
        try:
            cursor.execute(sql_6,)
            # sql_v=("SELECT * FROM CREDENTIALS WHERE ID={}".format())    
            # cursor.execute(sql_v,)
            a.commit()
            print("Member added successfully.")
        except Exception as e:
            print("Error:",e)
            print("Please enter any other username.")
            # pass
    # up=(username,password)
    # sql= ("INSERT INTO members(m_id,name,gender,age,email,height,weight,bmi,diet) VALUES('{}','{}','{}','{}','{}',' {}','{}','{}')").format(u_id,name,gender,age,email,height,weight,bmi,)
    # values=(name, gender, age, email, height, weight, bmi)
    # sql_1=("SELECT * FROM members NATURAL JOIN credentials")
    # try:
        # cursor.execute(sql,)
        # sql_v=("SELECT * FROM CREDENTIALS WHERE ID={}".format())    
        # cursor.execute(sql_v,)
        # a.commit()
        # print("Member added successfully.")
        
    # except Exception as e:
        # print("Error:",e)
        # print("Please enter any other username.")
        # pass
    # cursor.execute(sql_1)
    # u_id=register_user()
    # add_member()
    # for h in cursor:
    #     print(h[0])
    #     print(h[-1])

    return  name, gender, age, email, height, weight, bmi
    
    
    # Execute the SQL statement
def add_exercise_log(user_id):
    exercise_type = input("Enter exercise type: ")
    exercise_date = input("Enter exercise date (YYYY-MM-DD): ")
    duration_minutes = int(input("Enter exercise duration in minutes: "))
    calories_burned = int(input("Enter calories burned: "))

    # Prepare the SQL statement
    sql = "INSERT INTO exercise_log (user_id, exercise_type, exercise_date, duration_minutes, calories_burned) " \
          "VALUES (%s, %s, %s, %s, %s)"
    
    # Prepare the data to be inserted
    data = (user_id, exercise_type, exercise_date, duration_minutes, calories_burned)

    try:
        cursor.execute(sql, data)
        a.commit()
        print("Exercise log added successfully.")
    except Exception as e:
        print("Error:", e)
        print("Failed to add exercise log.")

    
def view_exercise_logs(user_id, choice):
    if choice == 1:
        # View all exercise logs for a user
        query = f"SELECT * FROM exercise_log WHERE user_id = {user_id}"
    elif choice == 2:
        # View logs by exercise type
        exercise_type = input("Enter the desired exercise type: ")
        query = f"SELECT * FROM exercise_log WHERE user_id = {user_id} AND exercise_type = '{exercise_type}'"
    elif choice == 3:
        # View logs by date range
        start_date = input("Enter the start date (YYYY-MM-DD): ")
        end_date = input("Enter the end date (YYYY-MM-DD): ")
        query = f"SELECT * FROM exercise_log WHERE user_id = {user_id} AND exercise_date BETWEEN '{start_date}' AND '{end_date}'"
    elif choice == 4:
        # View logs by duration range
        min_duration = int(input("Enter the minimum duration (in minutes): "))
        max_duration = int(input("Enter the maximum duration (in minutes): "))
        query = f"SELECT * FROM exercise_log WHERE user_id = {user_id} AND duration_minutes BETWEEN {min_duration} AND {max_duration}"
    elif choice == 5:
        # View logs by calories burned range
        min_calories = int(input("Enter the minimum calories burned: "))
        max_calories = int(input("Enter the maximum calories burned: "))
        query = f"SELECT * FROM exercise_log WHERE user_id = {user_id} AND calories_burned BETWEEN {min_calories} AND {max_calories}"
    else:
        print("Invalid choice.")
        print("Please enter a valid choice")
        return
    cursor.execute(query)
    result = cursor.fetchall()
    if result:
        print("Exercise Logs:")
        for row in result:
            print(row)
    else:
        print("No logs found for the selected criteria.")

def first_program():
    f_1="Diet Plan for Underweight: \n- Consume more calories than you burn\n- Eat a balanced diet with a variety of foods\n- Include protein-rich foods, whole grains, and healthy fats"

    # f_1_sql="INSERT INTO members(diet) VALUES('{}')".format(f_1)
    # cursor.execute(f_1_sql,)
    return f_1
    # list1 = ["You are Underweight."]
    # return list1

def second_program():
    f_2="Diet Plan for Normal Weight: \n- Maintain a balanced diet\n- Focus on portion control and moderation\n- Include fruits, vegetables, lean proteins, and whole grains"

    # f_2_sql="INSERT INTO members(diet) VALUES('{}')".format(f_2)
    # cursor.execute(f_2_sql,)       
    return f_2

def third_program():   
    # if bmi>=25.0 and bmi<=29.9:
    f_3="Diet Plan for Overweight: \n- Reduce calorie intake\n- Increase physical activity\n- Limit processed foods and sugar\n- Incorporate more fruits, vegetables, and lean proteins"
    # f_3_sql="INSERT INTO members(diet) VALUES('{}')".format(f_3)
    # cursor.execute(f_3_sql,)
    return f_3

def fourth_program():
    # if bmi>=30.0 and bmi<=34.9:
    f_4="Diet Plan for Obesity Class 1: \n- Aim to reduce daily calorie intake\n- Focus on portion control and reducing high-calorie foods\n- Include a variety of vegetables, lean proteins, and whole grains\n- Increase physical activity, aiming for at least 150 minutes of moderate-intensity exercise per week"

    # f_4_sql="INSERT INTO members(diet) VALUES('{}')".format(f_4)
    # cursor.execute(f_4_sql,)
    return f_4

def fifth_program():
    # if bmi>=35.0 and bmi<=39.9:
    f_5="Diet Plan for Obesity Class 2: \n- Consult a healthcare professional or a registered dietitian for a personalized plan\n- Significant weight loss may be necessary\n- Focus on reducing calorie intake and increasing physical activity\n- Emphasize a balanced diet with nutrient-dense foods"
    # f_5_sql="INSERT INTO members(diet) VALUES('{}')".format(f_5)
    # cursor.execute(f_5_sql,)
    return f_5

def sixth_program():
    # if bmi>=40.0 and bmi<=49.9:
    f_6="Diet Plan for Obesity Class 3: \n- Consult a healthcare professional or registered dietitian for a personalized plan\n- Emphasize weight loss through calorie reduction and increased physical activity\n- Focus on long-term lifestyle changes"

    # f_6_sql="INSERT INTO members(diet) VALUES('{}')".format(f_6)
    # cursor.execute(f_6_sql,)
    return f_6



# Function to view member details
# def view_member(username, password,id):

#     # Prepare the SQL statement
#     member_id=int(input("Enter the ID of the user to be viewed: "))
#     sql = "SELECT * FROM members WHERE id = %s"
    
#     # Prepare the data for the SQL statement
#     data = (member_id,)
    
#     # Execute the SQL statement
#     cursor = a.cursor()
#     cursor.execute(sql, data)
#     result = cursor.fetchone()
    
#     # Display member details
#     if result:
#         print("Member ID:", result[0])
#         print("Name:", result[1])
#         print("Age:", result[2])
#         print("Gender:", result[3])
#         print("Email:", result[4])
#         print("Height:", result[5])
#         print("Weight:", result[6])
#         print("BMI:", result[7])
#     else:
#         print("Member not found.")


def store(username, password, name, gender, age, email, height, weight, bmi):


    if bmi < 18.5:
        diet_1 = first_program()
    elif bmi>=18.5 and bmi<=24.9:
        diet_2 = second_program()
    elif bmi>=25.0 and bmi<=29.9:
         diet_3=third_program()
    elif bmi>=30.0 and bmi<=34.9:
        diet_4=fourth_program()
    elif bmi>=35.0 and bmi<=39.9:
        diet_5=fifth_program()
    else:
        diet_6=sixth_program()
        
    # Prepare the SQL statement

    sql = "INSERT INTO members (name, age, email, height, weight, bmi ) VALUES (%s, %s, %s, %s, %s, %s)"
    # Jenil_Project.bmi()
    # Prepare the data to be inserted
    data = (username, password, name, gender, age, email, height, weight, bmi )
    
    # Execute the SQL statement
    cursor = a.cursor()
    cursor.execute(sql, data)
    a.commit()

def modify():
    member_id = int(input("Enter member ID: "))
    
    # Prepare the SQL statement
    # sql = "SELECT * FROM members WHERE id = %s"
    
    # Prepare the data for the SQL statement
    # data = (member_id)
    
    # Execute the SQL statement
    # cursor = connection.cursor()
    # cursor.execute(sql, data)
    # result = cursor.fetchone()
    # -----------------------------
    while True:
        ch_=int(input("1.To modify age\n2.To modify email\n3.To modify height\n4.To modify weight\n5.Exit"))
        if ch_==1:
            m_age=int(input("Enter the value to be replaced: "))
            u_age=f"UPDATE members SET age={m_age} WHERE id={member_id}"
            cursor = a.cursor()
            cursor.execute(u_age)
        elif ch_==2:
            m_email=input("Enter the value to be replaced: ")
        elif ch_==3:
            m_height=float(input("Enter the value to be replaced: "))
        elif ch_==4:
            m_weight=int(input("Enter the value to be replaced: "))
        else:
             break



# ------------------------------------------
# print("----- Gym Management System -----")
# a=mysql.connector.connect(user="root",passwd="5685",host="localhost",database="gym")
# cursor=a.cursor()
# print("1. Please Enter 1 for Login ")
# print("2. Please Enter 2 for Signup")

# choice = int(input("Enter you choice: "))

# if choice == 1:
#     login_user.login_user()
#     # username = input("Enter Username: ")
#     # password = int(input("Enter Password: "))
#     # id = int(input("Enter your ID: "))
    
#     # # Validate user credentials
#     # sql = "SELECT * FROM credentials WHERE id=%s AND username=%s AND password=%s"
#     # values = (id, username, password)
#     # cursor.execute(sql, values)
#     # print(sql)
#     # result = cursor.fetchone()
#     # print(result)
#     while True:
#         print()
#         print("1. To view ")
#         print("2. To modify a member")
#         print("3. To delete a member")
#         print("4. To exit")
#         option=int(input("Eneter the option number : "))
#         if option==1:
#              pass
#         #     print("Login successful.")
#         #     print("Username:", username)
#         #     print("Password:", password)
            
#         #     # Fetch and display user information from the members table
#         #     sql_member = "SELECT * FROM members WHERE id=%s"
#         #     cursor.execute(sql_member, (id,))
#         #     member_result = cursor.fetchone()

#         #     if member_result:
#         #         print("Member Information:")
#         #         print("Name:", member_result[1])
#         #         print("Gender:", member_result[2])
#         #         print("Age:", member_result[3])
#         #         print("Email:", member_result[4])
#         #         print("Height:", member_result[5])
#         #         print("Weight:", member_result[6])
#         #         print("BMI:", member_result[7])
#         #     else:
#         #         print("Member information not found.")
#         elif option==2:
#              pass
#         elif option==3:
#              pass
#         else:
#              exit()
#         # else:
#             # print("Invalid credentials. Please try again.")
# else:           
#     add_member()
# # Close the database connection
# a.close()   
# Main program
print("----- Gym Management System -----")
while True:
    print("1. Sign Up")
    print("2. Login")
    print("3. Exit")
    
    choice = input("Choose an option (1/2/3): ")
    
    if choice == "1":
        register_user()
        
    elif choice == "2":
        x= login_user.login_user()
        if x!=None:
            user_id=x[1]
        # if user_id is not None:
            # Continue with the rest of your program
            # You can pass user_id to other functions as needed.
            while True:
                print()
                print("1. To modify a member")
                print("2. To delete a member")
                print("3. To enter data of exercise performed")
                print("4. To view exercise log")
                print("5. To exit")
                option=int(input("Enter the option number : "))
                # if option==1:
                #     print("1. View all logs")
                #     print("2. View logs of a specific member")
                #     slch=int(input("Enter your choice:"))
                #     if slch==1:
                #         pass
                if option==1:
                    print("--------------------------------------------")
                    print("List of items availabe for modification:")
                    print("1. Username")
                    print("2. Password")
                    print("3. Age")
                    print("4. Email")
                    print("5. Height")
                    print("6. Weight")
                    print("7. Exit")
                    while True:
                        sel_ch=int(input("Enter your choice for modification:"))
                        if sel_ch==1:
                            new_username = input("Enter the new username: ")
                            update_query = "UPDATE credentials SET username = '{}' WHERE id = '{}'".format(new_username, user_id)
                            cursor.execute(update_query)
                            a.commit()
                            print("Username updated successfully.")
                        elif sel_ch==2:
                            new_password = int(input("Enter the new password: "))
                            update_query = "UPDATE credentials SET password = {} WHERE id = '{}'".format(new_password, user_id)
                            cursor.execute(update_query)
                            a.commit()
                            print("Password updated successfully.")
                        elif sel_ch==3:
                            new_age = int(input("Enter the new age: "))
                            update_query = "UPDATE members SET age = {} WHERE m_id = '{}'".format(new_age, user_id)
                            cursor.execute(update_query)
                            a.commit()
                            print("Age updated successfully.")
                        elif sel_ch==4:
                            new_email = input("Enter the new email: ")
                            update_query = "UPDATE members SET email = '{}' WHERE m_id = '{}'".format(new_email, user_id)
                            cursor.execute(update_query)
                            a.commit()
                            print("Email updated successfully.")
                        elif sel_ch==5:
                            new_height = float(input("Enter the new height in meters: "))
                            update_query = "UPDATE members SET height = {} WHERE m_id = '{}'".format(new_height, user_id)
                            cursor.execute(update_query)
                            a.commit()
                            print("Height updated successfully.")
                        elif sel_ch==6:
                            new_weight = int(input("Enter the new weight in kg: "))
                            update_query = "UPDATE members SET weight = {} WHERE m_id = '{}'".format(new_weight, user_id)
                            cursor.execute(update_query)
                            a.commit()
                            print("Weight updated successfully.")
                        elif sel_ch==7:
                            break
                        else:
                            print("Oops! Invalid Choice.") 
                            print("Please enter a Valid Choice.")
                            
                elif option==2:
                    del_s=int(input("Enter the user id to delete:"))
                    d_s="DELETE FROM credentials WHERE id='{}'".format(del_s)
                
                elif option==3:
                    mid=int(input("Enter id of member to enter details:"))
                    add_exercise_log(mid)
                
                elif option==4:
                    while True:
                        print("1. To view all exercise logs")
                        print("2. To view logs by exercise type")
                        print("3. To view logs by date range")
                        print("4. To view logs by duration range")
                        print("5. To view logs by calorie burned range")
                        mid1=int(input("Enter id to view exercise logs of a member:"))
                        pfch=int(input("Enter your choice of viewing:"))
                        view_exercise_logs(mid1,pfch)

            
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

# Close the database connection
a.close()