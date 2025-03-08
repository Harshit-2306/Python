p1 = "Make a lot of money"
p2 = "Buy now"
p3 = "Subscribe this"
p4 = "Click this"

Message = input("Enter your comment : ")

if ((p1 in Message) or (p2 in Message) or(p3 in Message) or(p4 in Message)):
  print("This Comment is Spam")

else :
  print("This Comment is not Spam")