import mysql.connector
a=mysql.connector.connect(user="root",passwd="5685",host="localhost",database="gym")
cursor=a.cursor()
# cursor_execute=cursor.execute("create database jenil" )
# cursor.execute("create table Individual_Data(username varchar(30),password int(8),height int(3),weight int(3),bmi float(2,2),diet varchar(255))")
x=("insert into Individual_Data (username,password,height,weight,bmi,diet) values ('krutarth',123456,170,65,18,'abc')")
cursor.execute(x)
a.commit()
