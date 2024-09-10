L=[11,12,13,14]

#WAP to add 50 and 60 to L.
L.extend([50, 60])
print("List after adding 50 and 60:", L)

#WAP to remove 11 and 13 from L.
L.remove(11)
L.remove(13)
print("List after removing 11 and 13:", L)

# Sort L in ascending order
L.sort()
print("List sorted in ascending order:", L)

# Sort L in descending order
L.sort(reverse=True)
print("List sorted in descending order:", L)

# Search for 13 in L
search_value = 13
found = search_value in L
print(f"{search_value} is in the list:" if found else f"{search_value} is not in the list.")

# Count the number of elements in L
count = len(L)
print("Number of elements in the list:", count)

# Sum all elements in L
total_sum = sum(L)
print("Sum of all elements:", total_sum)

# Sum all odd numbers in L
odd_sum = sum(x for x in L if x % 2 != 0)
print("Sum of odd numbers:", odd_sum)

# Sum all even numbers in L
even_sum = sum(x for x in L if x % 2 == 0)
print("Sum of even numbers:", even_sum)

# Sum all prime numbers in L
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

prime_sum = sum(x for x in L if is_prime(x))
print("Sum of prime numbers:", prime_sum)

# Clear all elements in L
L.clear()
print("List after clearing:", L)

# Delete the list L
del L

L=[11,12,13,14]
#Write a Python program to sum all the items in a list without using any inbuilt function.
total_sum = 0
for number in L:
    total_sum += number
print("Sum of all items in the list:", total_sum)

#Write a Python program to multiply all the items in a list without using any inbuilt function.
total_product = 1
for numberr in L:
    total_product *= numberr
print("Product of all items in the list:", total_product)

D = {1: 5.6, 2: 7.8, 3: 6.6, 4: 8.7, 5: 7.7}

# WAP to add new entry in D; key=8 and value is 8.8
D[8] = 8.8
print("Dictionary after adding new entry:", D)

#WAP to remove key=2
if 2 in D:
    del D[2]
print("Dictionary after removing key 2:", D)

# WAP to check whether key 6 is present in D
key_to_check = 6
if key_to_check in D:
    print(f"Key {key_to_check} is present in the dictionary.")
else:
    print(f"Key {key_to_check} is not present in the dictionary.")

# WAP to count the number of elements present in D
num_elements = len(D)
print("Number of elements in the dictionary:", num_elements)

#WAP to add all the values present in D
total_value_sum = sum(D.values())
print("Sum of all values in the dictionary:", total_value_sum)

#WAP to update the value of key 3 to 7.1
if 3 in D:
    D[3] = 7.1
print("Dictionary after updating the value of key 3:", D)

#WAP to clear the dictionary
D.clear()
print("Dictionary after clearing:", D)

S1 = {10, 20, 30, 40, 50, 60}
S2 = {40, 50, 60, 70, 80, 90}

# WAP to add 55 and 66 in Set S1
S1.add(55)
S1.add(66)
print("Set S1 after adding 55 and 66:", S1)

# WAP to remove 10 and 30 from Set S1
S1.discard(10)  # discard does not raise an error if the element is not present
S1.discard(30)
print("Set S1 after removing 10 and 30:", S1)

# WAP to check whether 40 is present in S1
if 40 in S1:
    print("40 is present in Set S1.")
else:
    print("40 is not present in Set S1.")

# WAP to find the union between S1 and S2
union_set = S1.union(S2)
print("Union of S1 and S2:", union_set)

# WAP to find the intersection between S1 and S2
intersection_set = S1.intersection(S2)
print("Intersection of S1 and S2:", intersection_set)

# WAP to find the difference S1 - S2
difference_set = S1.difference(S2)
print("Difference of S1 - S2:", difference_set)

#Print 100 random strings with length between 6 and 8
import random
import string
num_strings = 100

for _ in range(num_strings):
    length = random.randint(6, 8)
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    print(random_string)

#Print all prime numbers between 600 and 800
for num in range(600, 801):
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

#Print all numbers between 100 and 1000 that are divisible by 7 and 9
for num in range(100, 1001):
    if num % 7 == 0 and num % 9 == 0:
        print(num)

#Write a Python program to display the examination schedule. (extract the date from exam_st_date). exam_st_date = (11, 12, 2014)
import datetime
exam_st_date = (11, 12, 2014)
exam_date = datetime.date(exam_st_date[2], exam_st_date[1], exam_st_date[0])
print("The examination will start on:", exam_date.strftime("%d %b %y"))

#Iterate the given list of numbers and print only those numbers which are divisible by 5.
numberss = [10, 23, 45, 67, 80, 91, 100, 115, 134, 150]
for numberrr in numberss:
    if numberrr % 5 == 0:
        print(numberrr)

#Create a new list from two list using the following condition, Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [10, 11, 12, 13, 14, 15, 16, 17, 18]
new_list = [num for num in list1 if num % 2 != 0] + [num for num in list2 if num % 2 == 0]
print("New list:", new_list)
