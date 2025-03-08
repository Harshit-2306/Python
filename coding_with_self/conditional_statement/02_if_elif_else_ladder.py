a = int(input("Enter a age : "))

if(a>18):
 print("You are above the age of consent")

elif(a<0):
 print("you are entering an invalid age ")

elif(a == 0):
 print("you are entering 0 that is not valid ")

else:
 print("You are below the age of consent")

print(type(a))