# Spatial Programming Lab 02: Python language fundamentals
# Seth Opatz
# 03/25/2025

# Question 1
print("\nQuestion 1:") #'\n' is the newline character
length = 30
meter_length = length * 0.3048
print("30 feet in meters = " + str(meter_length))

# Question 2
print("\nQuestion 2:")
score1 = 90
score2 = 80
print(f"The sum of these scores is {score1 + score2}.")
print(f"Their average is {(score1 + score2) / 2}.")

# Question 3
print("\nQuestion 3:")
numbers = [1, 32, 17, 46, 23, 10]
numbers.sort() #sort list in ascending order
print(f"The second largest number of the list is {numbers[len(numbers) - 2]}") #get element at index second from the end

# Question 4
print("\nQuestion 4:")
test1 = [15, 10, 8, 23, 15, 12, 28, 10]
test2 = [2, 8, 12, 25, 28, 13, 21, 15]

# Boolean function to check for duplicates
def duplicate_checker(number_list):
    number_list.sort()
    last_number = None #declaring last_number variable with nothing in it for now
    for number in number_list:
        if number == last_number:
            return True
        last_number = number
    return False

# Print results for test1
if duplicate_checker(test1):
    print("List test1 contains duplicate values")
else:
    print("List test1 does not contain duplicate values")

# Print results for test2
if duplicate_checker(test2):
    print("List test2 contains duplicate values")
else:
    print("List test2 does not contain duplicate values")

# Question 5
print("\nQuestion 5:")
geoid = "1400000US39129021402"
us_index = geoid.find("US") #find index in string where 'US' happens
if us_index != -1:
    substring = geoid[us_index+2:] #creates substring from 2 indices after 'US' is found to the end of the string
    print(substring)
else: print("'US' not found in GEOID")

# Question 6
print("\nQuestion 6:")
Beatles = ["John Lennon", "Paul McCartney", "Ringo Starr", "George Harrison"]
print(f"The list contains {len(Beatles)} names.")
print(f"The third member of the band is {Beatles[2]}.")
print("The last name of each band member is: ")
for member in Beatles:
    print(member.split()[-1]) #split each name on a space and print the last element of each resulting list

# Question 7
print("\nQuestion 7:")
import random
num1 = random.randint(1, 6)
num2 = random.randint(1, 6)
print(f"First random number (1-6): {num1}")
print(f"Second random number (1-6): {num2}")
difference = num2 - num1
print(f"2nd number - 1st number = {difference}")
if difference < 0:
    print("You lose.")
elif difference > 0: #"else if" statement
    print("Try again.")
else: #if the difference is zero
    print("You win!")

# Question 8
print("\nQuestion 8:")
for i in reversed(range(11)): #loops through reversed list of numbers from 10 to 0
    print(i)