#Print is a function which is used to print everthing and perform any kind of operations

print("Hello World")
print(2+3)
print(15-12)

# Single Line Comment

'''
Multi
Line 
Escaping
Comment
'''

#These are used to ignore 1 or few lines from the code

#This is addition
print(1+2)

#Each and everyline is getting omitted


# A variable is a thing in python which can store anything into it.(No matter how big is it!!)

a = "Hello World" # Hello World is Stored in variable a
print(a) # By printing the variable , it will give that stored part in output

b = 1124  #Integer Variable
print(b)

c = 12.566 #Float Variable
print(c)

#Operations
a = 10
b = 2.5
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#String Connecting
a = "Hello"
b = "How are you"
print(a+b)

#No operations take place in a string if number is given
a = "10"
b = "12"
print(a+b)

#Typecasting
a = "10"
b = "12"
print(int(a)+int(b)) #integer function is used to add two given numbers in a string(int)

#More Functions
"""
print()
str()
int()
eval()
float()
type()
input()
len()
"""
#printing multiple times
print(5 * "Hi") #Hi will be printed 5 times

#converting to a string
a = "35"
b = "35"
print( 10 * str (int(a)+int(b)))

#User input
a = input("Enter a Number : ") #It is stored as a String in variable a
print(a)

#Printing String
str = "Hi , I am Bitashok"
print(str)

#Slicing the string
str = "Hi , I am Bitashok"
print(str[0:18]) #1 is the index number. Index Number is the specific number of each elements in this given string.
#It starts from 0

str = "Hi , I am Bitashok"
print(str[0:3]) # 0:3 is the range upto which you want to print the elements of string

#Length of string
str = "Hi , I am Bitashok"
print(len(str))
#len is a function which is used to the length of the string , that is , the exact number of characters
#Characters include spaces and syntax also

#Escaping Characters
str = "Hi , I am Bitashok"
print(str[0:18:2]) #Each and every 2nd element of the string will be escaped
#This is called String Element Escaping

#Negative Indexing
str = "Hi , I am Bitashok"
print(str[-1:-9]) #the "-" index starts from the Last element of the string
#This is also known as Reverse Slicing

#Reversing the whole string
str = "Hi , I am Bitashok"
print(str[::-1])

#Functions
str = "Hi , I am Bitashok"
print(str.isalnum()) #It will give output as False as spaces are ther between elements
#Output will come as True when there will be no spaces between the elements of the string
str = "Hi , I am Bitashok"
print(str.isalpha())
str = "Hi , I am Bitashok"
print(str.endswith("Bitashok")) # As the string is ending with Bitashok , It will show True
str = "Hi , I am Bitashok"
print(str.count("i")) # It will count the Number of provided element in the given string
str = "hi , i am bitashok"
print(str.capitalize()) # It will capitalize the first element
str = "Hi , I am Bitashok"
print(str.find("is")) #It Will find the index number of the first element of the word which you want to find
str = "Hi , I am Bitashok"
print(str.lower()) #It will convert every element into lower case elements
str = "Hi , I am Bitashok"
print(str.upper())#It will convert every element into upper case elements
str = "Hi , I am Bitashok"
print(str.replace("Hi","Hello"))#It will replace the word which user wants to input

'''More functions are there which are available in Google'''
