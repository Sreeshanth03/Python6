# iv. 	 Write a program to find the greatest of two numbers
# n=int(input("enter the first number:"))
# m=int(input("enter the second number:"))
# if(m>n):
#     print("The greatest number is",m)
# else:
#     print("The greatest number is",n)

# v.	Print "Pass" if a student scores more than 40 marks;  otherwise, print "Fail." 
# n=int(input("Enter the Marks:"))


# if(n>=40):
#     print("Pass")
# elif(n<40):
#     print("Fail")

# vi.	Write a program to display the day of the week based on a  number input (1 for Monday, 2 for Tuesday, etc.). 

# n=int(input("Enter the Week:"))
# if(n==1):
#     print("Monday")
# elif(n==2):
#     print("Tuesday")
# elif(n==3):
#     print("Wednesday")
# elif(n==4):
#     print("Thursday")
# elif(n==5):
#     print("Friday")
# elif(n==6):
#     print("Saturday")
# elif(n==7):
#     print("Sunday")

# **********FizzBuzz********
# n=int(input("Enter the number:"))
# if(n%15==0):
#     print("FizzBuzz")
# elif(n%3==0):
#     print("Fizz")
# elif(n%5==0):
#     print("Buzz")
# else:
#     print("Invalid")

# vii.	Implement a simple calculator to perform addition,  subtraction, multiplication, and division. 

# num1=int(input("Enter The First Number:"))
# num2=int(input("Enter The Second Number:"))
# x=input("Enter(+,-,*,/,add,sub,mul,div):").lower()
# if x in ["add","a","ADD","ad","+"]:
#     print(num1+num2)
# elif x in ["-","Sub","a",]:
#     print(num1-num2)
# elif x in ["*","mul","MuL"]:
#     print(num1*num2)
# elif x in ["/","div","Div"]:
#     print(num1/num2)
# else:
#     print("Invalid")

# viii.	Write a program to display the name of a month based on  the month number (1 for January, 2 for February, etc.). 

# n=int(input("Enter the number:"))
# if(n==1):
#     print("Jan")
# elif(n==2):
#     print("Feb")
# elif(n==3):
#     print("Mar")
# elif(n==4):
#     print("April")
# elif(n==5):
#     print("May")
# elif(n==6):
#     print("June")
# elif(n==7):
#     print("July")
# elif(n==8):
#     print("August")
# elif(n==9):
#     print("Sep")
# elif(n==10):
#     print(Oct)
# elif(n==11):
#     print("Nov")
# elif(n==12):
#     print("Dec")
# else:
#     print("Invalid")

# b.  Medium Questions: 
# i.	Write a program to find the greatest of three numbers. 
# x=int(input("Enter The First Number:"))
# y=int(input("Enter The Second Number:"))
# z=int(input("Enter The Thrid Number:"))
# if(x>y and x>z):
#     print("The Greatest Number is",x)
# elif y > x and y > z:
#     print("The Greatest Number is", y)
# elif z > x and z > y:
#     print("The Greatest Number is", z)
# else:
#     print("The input is Invalid")

# ii.	Check if a year is a leap year. 
# n=int(input("Enter The Year:"))
# if(n%4==0 and n%100 !=0 and n%400==0):
#     print("Its is a Leap Year")
# else:
#     print("Its not a leap year")

# iii.	Write a program to classify a character entered by the user  as a vowel, consonant, or neither. 

# n=input('Enter:').lower()
# if n in ["a","e","i","o","u"]:
#     print("It is a  Vowels")
# else:
#     print("It does not vowels")

# iv.	Calculate the grade of a student based on the marks they  score: 
# 1.	90-100  : Grade A 
# 2.	80-89  : Grade B 
# 3.	70-79  : Grade C 
# 4.	<70  : Fail. 


#  v. 	 Write a program to check if three sides length form a valid  triangle. 

# x=int(input("Enter the x:"))
# y=int(input("Enter the y:"))
# z=int(input("Enter the z:"))
# if(x+y>z and y+z>x and x+z>y):
#     print("The Triangle is possible")
# else:
#     print("Invalid Triangle")
# for i in range(0,100):
#     printI(i)


# # ii.	Write a program to print the sum of the first  n  natural  numbers. (n*n+1/ 2) 
# n=int(input("Enter the following:"))
# sum=(n * (n + 1)) // 2
# print(f"Sum of the first {n} natural numbers is: {sum_natural}")


# sum=0;
# i=1;
# while i<50:
#     if(i%2==0):

#         sum+=2
#     i+=1
# print(sum)


# n=int(input("Enter the number:"))
# for i in range(0,21):
#             print(i*n)


# v.	Reverse a number using a  	 while  loop. 
#  1.  Also can we get the sum of all the digits.  


# i=10;
# sum=0
# for i in range(10,0,-1):
#     sum+=i
#     print(sum)

# 	 Write a program that keeps asking the user to enter numbers  until they enter a negative number. Use a  while  loop. 
# n=int(input("Enter the number:"))
# for i in range(0,1):
#     if(n<0):
#         print("You Entered a wrong number")
#     else:
#         print("Entered Correct Number")



# i.	Print the first 10 terms of the Fibonacci series using a  for  loop. 
# n=0
# m=1
# for i in range(1,10):
#     temp=n+m
#     n=m
#     m=temp
#     print(n)

# iii.	Write a program to calculate the factorial of a number using  a  while  loop.  
# i=1
# fact=1
# while i<10:
#     fact*=i
#     i+=1
#     print(fact)

# iv. 	 Print all numbers from 1 to 100 that are divisible by 3 and 5  using a  for  loop. 
# for i in range(0,100):
#     if(i%5==0 and i%3==0):
#         print(i)
# n=int(input("Enter the number:"))
# if(n%2==0):
#     print("its a prime number")
# else:
#     print("oddddddddddd")
                                                                # **pizza**
# size=(input("Enter the size of the Pizza S/M/L?:"))
# bill=0
# if size=="S" or size=="s":
#     bill+=100
#     print("the pizza is for 100 rupeess")
# elif size=="M" or size=="m":
#     bill+=200
#     print("the medium pizza is for 200 rupees")
# else:
#     bill+=300
#     print("you choosed large pizza")
# add_pepperoni=(input("Do you want to add pepperoni y/n?:"))
# if add_pepperoni=="Y" or add_pepperoni=="y":
#     if size=="S" or size=="s":
#         bill+=30
    

# extra_cheese=input("Do you Want extra cheese y/n")
# if extra_cheese=="M" or extra_cheese=="m":
#     bill+=30
# print(f"your final is {bill}")
# ***pratice***
# numbers=[10,20,30,40,50]
# for i in numbers:
#     print(i)

# num=0
# for i in range(1,51):
#    num+=i
# print("The sum of the 50 numbers is:",num)

# n=int(input("Enter The Table:"))
# for i in range(1,21):
#         print(n,"*",i,"=",n*i)


# fact=1
# n=int(input("Enter The Factorial:"))
# for i in range(1,n+1):
#     fact*=i;
# print("The Fact of ",n,"is",fact)

# rev a number:

# num1 = int(input("Enter a number: "))  
# count = 0
# sum_digits = 0
# rev_num = 0

# while num1 > 0:
#     r = num1 % 10 
#     print( r)

#     rev_num = rev_num * 10 + r 
#     num1 = num1 // 10  
#     count += 1 
#     sum_digits += r  
# print("Reverse :", rev_num)
# print("Count :", count)
# print("Sum :", sum_digits)





