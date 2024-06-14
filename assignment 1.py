#1. write a program that takes two numbers as input and prints their sum
a=int(input("enter ist number:"))
print("the ist number is:",a)
b=int(input("enter 2nd number:"))
print("the 2nd number is :",b)
c=a+b
print("the sum of two digits is:",c)

#2. write a python program that checks whether a given number is even or odd.
x=8
if (8%2)==0:
    print(x,"Is Even Number")
else:
    print(x, "Is Odd Number")

#3. write a python program that calculates the facotorial of a given number:
num = int(input("Enter a number: "))    
factorial = 1    
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       factorial = factorial*i    
   print("The factorial of",num,"is",factorial)    

#4.write a program that asks the user for their name and then prints a greeting message
name=input("enter the name:")
print("good morning",name)
 
#5. temp = input("Please enter your information!!   ") 
try: 
    with open('gfg.txt', 'w') as gfg: 
        gfg.write("temp") 
except Exception as e: 
    print("There is a Problem", str(e)) 

#6. write a program that reads the content of a text file and prints it to console
file_path = 'sample.txt'
 
try:
    with open(file_path, 'r') as file:
        # Read the content of the file
        file_content = file.read()
         
        # Print the content
        print("File Content:\n", file_content)
 
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

#7.write a program that takes a string as input and returns its length
name=input("enter the name")
print(len[name])

#8. write a python program that concatenates two string and returnd the result python
str1 = "Hello "
str2 = "Coders"
str3 = str1 + str2
print("The new combined string is:",str3)

#9. write a python program that checks if a substring is present in a giveb string
MyString1 = "A geek in need is a geek indeed"
  
if "need" in MyString1: 
    print("Yes! it is present in the string") 
else: 
    print("No! it is not present") 

#10. write a python program that converts string into uppercase
name=input("enter the name:")
print(name.uppercase)

#11. Write a Python program that generates the first n numbers in the Fibonacci sequence.
def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]


#12. Write a Python program that calculates the sum of the digits of a given number.
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))


#13. Write a program that asks the user for their birth year and calculates their age.
def calculate_age():
    birth_year = int(input("Enter your birth year: "))
    current_year = 2024  # update this to the current year
    age = current_year - birth_year
    print("Your age is", age)


#14. Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
def read_and_print_lines():
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    print("\n".join(lines))


#15. Write a program that reads data from a CS file and prints it to the console.
def read_cs_file(filename):
    with open(filename, "r") as file:
        print(file.read())


#16. Write a program in Python that counts the frequency of each character in a string.
def char_frequency(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency


#17. Write a program in Python that converts a given string to title case (first letter of each word capitalized).
def title_case(string):
    return string.title()


#18. Write a Python program that checks if two strings are anagrams of each other.
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)


#19. Write a Python program that removes all punctuation from a given string.
def remove_punctuation(string):
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    for char in string:
        if char in punctuation:
            string = string.replace(char, "")
    return string


#20. Write a Python program that takes a list of numbers and returns their sum.
def sum_of_list(numbers):
    return sum(numbers)


#21. Write a Python program that counts the occurrences of a specific element in a list.
def count_occurrences(lst, element):
    return lst.count(element)


#24. Write a Python program that returns the minimum and maximum values in a list of numbers.
def find_min_max(numbers):
    return min(numbers), max(numbers)


#23. Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.
def convert_temperature():
    choice = input("Enter 'C' for Celsius to Fahrenheit or 'F' for Fahrenheit to Celsius: ")
    temperature = float(input("Enter temperature value: "))

    if choice.upper() == 'C':
        result = (temperature * 9/5) + 32
        print(f"{temperature}°C is equal to {result}°F")
    elif choice.upper() == 'F':
        result = (temperature - 32) * 5/9
        print(f"{temperature}°F is equal to {result}°C")
    else:
        print("Invalid choice. Please enter 'C' or 'F'.")


#24. Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.
def simple_calculator():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero!")
            return
    else:
        print("Invalid operator. Please enter +, -, * or /.")
        return

    print("Result:", result)


#25. Write a program that copies the contents of one text file to another.
def copy_file_contents(source_file, destination_file):
    with open(source_file, 'r') as src_file:
        content = src_file.read()
    
    with open(destination_file, 'w') as dest_file:
        dest_file.write(content)


#26.rite a program in Python that checks if a string starts with a given prefix or ends with a given suffix.
def check_prefix_suffix(string, prefix, suffix):
    if string.startswith(prefix):
        print(f"'{string}' starts with '{prefix}'")
    else:
        print(f"'{string}' does not start with '{prefix}'")
    
    if string.endswith(suffix):
        print(f"'{string}' ends with '{suffix}'")
    else:
        print(f"'{string}' does not end with '{suffix}'")


#27. Write a program in Python that converts a string into a list of its characters.
def string_to_list(string):
    return list(string)








