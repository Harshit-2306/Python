# #WAP to print a palindrome number

# num = int(input("Enter a number: "))
# temp = num
# rev = 0
# while num > 0:
#     dig = num % 10
#     rev = rev * 10 + dig
#     num = num // 10
    
#     if temp == rev:
#         print("The number is a palindrome!")
#     else:
#         print("The number is not a palindrome!")
#         break
       
num = int(input("Enter a number: "))
temp = num  # Store the original number
rev = 0

while num > 0:
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10  # Integer division

# Check if original number and reversed number are the same
if temp == rev:
    print("The number is a palindrome!")
else:
    print("The number is not a palindrome!")

       