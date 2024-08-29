# Write a program that prints the numbers from 1 to 20. For 
# each number, print "Even" if the number is even and "Odd" if the number is odd.

for i in range(1, 21, 1):
    if i %2==0 :
        print("even")
    else:
        print("odd")
#Write a program that iterates through a list of numbers and prints whether each number is 
# "Positive" or "Negative". Include 
#zero in the list as well and classify it as "Zero".

for i in range(-1, 11, 1):
    if i > 0 :
        print("positive")
    else:
        print("negative")
