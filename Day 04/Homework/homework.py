#მომხმარებელს  შემოატაინე შენი სახელი და ასაკი გვარი  და საცხოვრებელი ადგილი შემდეგ გაკეთე ერთი დიდი წინადადება
#
name=input("what is your name ")
lastname=input("enter your last name ")
age=input("enter your age ")
address=input("where do you live ")                               

print(name + " " +lastname + " is " + age + " years old and live in " + address)

#მომხმარებელს შემოატაინე  შენი ასაკი , და შენი მშობლის ასაკი შემდეგ გამოთვალე რამდენი წლით დიდია შნეზე შენი მშობელი
#task 2

age1=input("enter your age ")
age2=input("enter moms age ")
age3=input("enter dads age ")


print(int(age2) - int(age1) )
print(int(age3) - int(age1) )