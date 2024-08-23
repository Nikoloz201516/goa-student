"""6)  input() ფუნქციის დახმარებით მომხმარებელს შემოაქვს ორი რიცხვი a და b.
 for ციკლის გამოყენებით ტერმინალში გამოიტანეთ რიცხვები a-დან b-მდე ( range(a, b) )"""
a=int(input("enter a number"))
b=int(input("ENTER A NUMBER"))
for i in range(a,b,1):
    print(i)