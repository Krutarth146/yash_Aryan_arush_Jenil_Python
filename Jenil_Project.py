user_name = "jenil"
password = "abc123"
flag = True
while flag:

    entered_user_name = input("Enter Username : ")
    entered_password = input("Enter Password : ")
    
    if entered_password == password and entered_user_name == user_name:
        flag = False
        print("Login successful!!")
        print("For conversion of your height into cm")
        height_in_centimetres=int(input("Enter your height in cm : "))
        h1=height_in_centimetres/100
        print("Your height in m is :",h1,"m")
        height = input("enter your height in metres: ")
        weight = input("enter your weight in kg: ")

        weight_as_int = int(weight)
        height_as_float = float(height)


        bmi = weight_as_int / height_as_float ** 2

        bmi = weight_as_int / (height_as_float * height_as_float)

        bmi_as_int = int(bmi)
        x=("insert into Individual_Data (username,password,height,weight,bmi,diet) values ( entered_user_name, entered_password, height_as_float, weight_as_int,  bmi_as_int,diet))")

        print("Your Body Mass Index is: ",bmi_as_int)
      
        if bmi_as_int<18.5:
            print("You are Underweight.")
            print("You should include following items in your diet:")
            print("1 - Whole Milk")
            print("2 - Plenty of protein supplements")
            print("3 - Carbohydrates")
            print("4 - Cheese and other dairy products")
            print("You will also have to burn minimum 50 percentage of the total calorie intake.")

        if bmi_as_int>=18.5 and bmi_as_int<=24.9:
            print("Your BMI is normal.")
            print("You should include following items in your diet:")
            print("1 - Whole Milk")
            print("2 - Adequate of protein supplements")
            print("3 - Carbohydrates")
            print("You will also have to maintain your current calorie intake ratio and calorie burn ratio.")

        if bmi_as_int>=25.0 and bmi_as_int<=29.9:
            print("You are Overweight.")
            print("You should include following items in your diet:")
            print("1 - Milk with least fats")
            print("2 - Plenty of fibre rich supplements")
            print("3 - Fruits with good amount of fibre and water content")
            print("4 - Instead of wheat and rice have bajra and oats")
            print("You will also have to burn minimum 80 percentage of the total calorie intake.")
        
        if bmi_as_int>=30.0 and bmi_as_int<=34.9:
            print("You are in Obesity Class 1.")
            print("You should include following items in your diet:")
            print("1 - Milk with least fats")
            print("2 - Plenty of fibre rich supplements")
            print("3 - Fruits with good amount of fibre and water content")
            print("4 - Instead of wheat and rice have bajra and oats")
            print("You will also have to burn minimum 90 percentage of the total calorie intake.")
        
        if bmi_as_int>=35.0 and bmi_as_int<=39.9:
            print("You are in Obesity Class 2.")
            print("You should include following items in your diet:")
            print("1 - Milk with least fats")
            print("2 - Plenty of fibre rich supplements")
            print("3 - Fruits with good amount of fibre and water content")
            print("4 - Instead of wheat and rice have bajra and oats")
            print("You will also have to burn minimum 100 percentage of the total calorie intake.")
            print("Also if consult a doctor if required.")

        if bmi_as_int>=40.0 and bmi_as_int<=49.9:
            print("You are in Obesity Class 3.")
            print("Consult a doctor at the earliest.")
    else:
        print("Login unsuccessful!!")
        print("Try again")