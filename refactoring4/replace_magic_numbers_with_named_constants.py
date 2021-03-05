# by Kami Bigdely 
# Replace magic numbers with named constanst

# First Section
# Given two point charges, calcualte the electric force exerted on them.
NEWTON = 8.9875517923*1e9

q1 = int(input('Enter a value of charge q1: '))
q2 = int(input('Enter a value of charge q2: '))
distance = int(input("Enter the distance between two charges: "))
force = NEWTON * q1 * q2/(distance**2)
print ("Electric Force between q1 and q2 is: ", force, "Newton")


# Second Section
SMALLEST_EVEN_NUM = 2
NO_REMAINDER = 0

num = int(input('Enter an integer number: '))
if num % SMALLEST_EVEN_NUM == NO_REMAINDER:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")