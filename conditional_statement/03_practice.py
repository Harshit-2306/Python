a = int(input("enter a number : "))
b = int(input("enter a number : "))
c = int(input("enter a number : "))
d = int(input("enter a number : "))

if(a>b and a>c and a>d):
 print("the greater number is a : ", a)

elif(b>a and b>c and b>d):
 print("the greater number is b : ", b)

elif(c>b and c>a and c>d):
 print("the greater number is c : ", c)

else:
 print("the greater number is d : ", d)