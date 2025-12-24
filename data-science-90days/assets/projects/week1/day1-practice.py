# name = "Arbythecoder"
# age = 25
# location = "Earth"

# def greet_user(name, age, location):
#     print(f"Hello, {name}! You are {age} years old and live on {location}.")

# greet_user(name, age, location)
# def update_location(new_location):
#     global location
#     location = new_location
#     print(f"Location updated to {location}.")
#     greet_user(name, age, location)

# update_location("Mars")
# update_location("Venus")
# # string , boolean , integer, float,list,dictionary 
# #  a list is a collection  of items that can be changed while tuple is collection of times that cannot change.
# # string

# name ="Arbythecoder"
# mother = "Adebimpe"
# location = "ikeja"
# # boolean
# my_float = 0.14
# my_perfect = 3.0
# desktop =12.14
# # boolean
# boolean_value = True
# listing =False
# dealer = True


# # arithimetic operations
# new = 2 + 2
# five_minus_three = 5 - 3
# five_minus_one = 5 - 1

# # comparison operations
# five_greater_than_three = 5 > 3
# five_less_than_thirty_three = 5 < 33
# ten_equals_one = 10 == 1

# # using type() to check the data types of each variable
# naming  = type(name)
# mothering = type(mother)

# # what input() means
# # input() is a built-in function in Python that allows you to take input from the user.
# # It pauses the program and waits for the user to type something into the console.
# hello = input("What's your name? ")
# age = input("How old are you? ")



# #convert age from string to integer
# age = int(age)

# # print welcome message
# print(f"Hello {hello}, you are {age} years old.")

# # erros gotten from adding a number to a string
# name = "Arbythecoder" + age
# # print(name)  # This will raise a TypeError because you cannot concatenate a string and an integer directly.

# arithimetic
a = 10
b = 25
c = 12
# addition
plus = a + b
# subtraction
minus = b - c
# multiplication
multiply = a * c
# division
divide = b / a
print(f"Addition: {plus}, Subtraction: {minus}, Multiplication: {multiply}, Division: {divide}")

# comparison
a > b #false
b > c #true
a < c #false
b == c #false
# input/output
age = input("Enter your age: ")
age = int(age)  # Convert the input string to an integer
print(f"Arby, you are {age} years old.")

# miniproject

def your_name():
    name = input("Enter your name: ")
    return name

def your_age():
    age = input("Enter your age: ")
    return int(age)

def your_location():
    location = input("Enter your location: ")
    return location

def your_favorite_color():
    color = input("Enter your favorite color: ")
    return color

print("Welcome to the mini project!")
name = your_name()
age = your_age()
location = your_location()
favorite_color = your_favorite_color()

print(f"Hello {name}! You are {age} years old, live in {location}, and your favorite color is {favorite_color}.")

# update_location = input("Do you want to update your location?

location = 'lagos'

def update_location(new_location):
    global location
    location = new_location
    print('before update:', location)
    update_location('abuja')
    print('after update:', location)    