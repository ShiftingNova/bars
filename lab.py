# Jordan Walker CSC110 this code takes an imput and creates a bar thing and puts # on the left side of the bar
code = str(input("Enter bar string:\n"))
print("+---------+")
i = 0
while i<len(code):
   print("|"+ "#" * int(code[i]) + " " * (9-int(code[i])) + "|")
   i = i +1
print("+---------+")
