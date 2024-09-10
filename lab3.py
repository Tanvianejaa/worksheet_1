#Write a Python program to calculate the difference between a given number and 17 with the help of function. If the number is greater than 17, return twice the absolute difference.
def calculate_difference(num):
    abs_diff = abs(num - 17)
    if num > 17:
        return 2 * abs_diff
    else:
        return abs_diff
number = float(input("Enter a number: "))
result = calculate_difference(number)
print(f"The result is: {result}")

#Write a Python program for a function. to test whether a number is within 100 to 1000 or 2000.
def check_range(num):
    if 100 <= num < 1000:
        print("The number is in the range 100-1000.")
    elif 1000 <= num < 2000:
        print("The number is in the range 1000-2000.")
    else:
        print("The number is not in the range 100-1000 or 1000-2000.")
number = float(input("Enter a number: "))
check_range(number)

#Write a Python program to reverse a string.
def reverse_string_slicing(s):
    return s[::-1]
input_string = input("Enter a string: ")
reversed_string = reverse_string_slicing(input_string)
print(f"Reversed string: {reversed_string}")

#Write a Python function that accepts a string and counts the number of upper and lower case letters
def count_case_letters(s):
    uppercase_count = 0
    lowercase_count = 0
    for char in s:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
    return uppercase_count, lowercase_count
input_string = input("Enter a string: ")
upper_count, lower_count = count_case_letters(input_string)
print(f"Uppercase letters: {upper_count}")
print(f"Lowercase letters: {lower_count}")

#Write a Python function that takes a list and returns a new list with distinct elements from the first list.
def get_distinct_elements(lst):
    distinct_set = set(lst)
    distinct_list = list(distinct_set)
    return distinct_list
input_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
distinct_list = get_distinct_elements(input_list)
print(f"List with distinct elements: {distinct_list}")

#Write a Python program to print the even numbers from a given list. Sample List : [1,2, 3, 4, 5, 6, 7, 8, 9]
def print_even_numbers(lst):
    print("Even numbers in the list are:")
    for num in lst:
        if num % 2 == 0:
            print(num)
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print_even_numbers(sample_list)

#Write a Python program to access a function inside a function
def outer_function():
    def inner_function():
        print("hy tanvi")
    inner_function()
outer_function()

#Define a Python function student(). Using function attributes display the names of all arguments.
def student(name, class_, roll_no):
  
    pass 

def display_argument_names(func):
    code_obj = func.__code__
    arg_names = code_obj.co_varnames[:code_obj.co_argcount]
    print("Argument names of the function:")
    for arg in arg_names:
        print(arg)
display_argument_names(student)

#Write a Python class named Student with two attributes: student_id, student_name. Add a new attribute: student_class. Create a function to display all attributes and their values in the Student class.
class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

    def display_attributes(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")
        print(f"Student Class: {self.student_class}")
student1 = Student(student_id=123, student_name="Tanvi", student_class="10th Grade")
student1.display_attributes()

#Write a Python class named Student with two instances student1, student2 and assign values to the instances' attributes. Print all the attributes of the student1, student2 instances with their values in the given format.
class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

    def display_attributes(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")
        print(f"Student Class: {self.student_class}")

student1 = Student(student_id=101, student_name="Alice", student_class="10th Grade")
student2 = Student(student_id=102, student_name="Bob", student_class="12th Grade")

print("Attributes of student1:")
student1.display_attributes()


print("\nAttributes of student2:")

student2.display_attributes()

# Write a Python class named Circle constructed from a radius and two methods that will compute the area and the perimeter of a circle.
class Circle:
    PI = 3.14
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.PI * (self.radius ** 2)

    def perimeter(self):
        return 2 * Circle.PI * self.radius

circle = Circle(radius=5.0)

print(f"Circle with radius: {circle.radius}")
print(f"Area: {circle.area()}")
print(f"Perimeter: {circle.perimeter()}")

#Write a Python class that has two methods: get_String and print_String , get_String accept a string from the user and print_String prints the string in upper case.
class StringProcessor:
    def __init__(self):
        self.user_string = ""
    
    def get_string(self):
        self.user_string = input("Enter a string: ")
    
    def print_string(self):
        print(self.user_string.upper())

processor = StringProcessor()
processor.get_string()  
processor.print_string()  
