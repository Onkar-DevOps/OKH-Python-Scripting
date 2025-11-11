#Subscripting
print("Hello"[0]) #H
print("Hello"[4]) #o    

#String
print("Hello"[0:3]) #Hel
print("Hello"[1:4]) #ell
print("123" + "345") #123345

#Integer
print(123 + 345) #468

#Float
print(3.14 + 4.56) #7.7

#Boolean
print(True) #True
print(False) #False

#larger datatype
print(123_456_789) #123456789

#Type function returns the datatype of the value
print(type(123)) #<class 'int'>
print(type(3.14)) #<class 'float'>
print(type("Hello")) #<class 'str'>
print(type(True)) #<class 'bool'>

#conversion between datatypes
print(int(3.14)) #3
print(float(123)) #123.0
print(str(456)) #"456"
print(bool(0)) #False

#The comma makes print convert the int to a string and separate them with a space — no error.
print ("Number of characters in your name: ", + len(input("Enter your name: ")), len(input("Enter your Surname: "))) #5

# It tries to concatenate a str and an int with +, As there is no comma.
#print("Number of letters in your name: " + (len(input("Enter your name: ")))

#Fix it using str function to convert int to str.
print("Number of letters in your name: " + str(len(input("Enter your name: "))))

#F string function is used convert multiple datatype to string
score = 25
rr = 55.78
name = "onkar"

print(f"Your name is {name} and score is {score} and runrate is {rr}")