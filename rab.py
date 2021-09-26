# Jordan Walker CSC110 this code does the same thing as lab but instteead of putting # on the left its on the right
code = str(input("Enter bar string:\n"))
print("+---------+")
i = 0
while i<len(code):
   print("|"+ " " * (9-int(code[i])) + "#" * int(code[i]) + "|")
   i = i +1
print("+---------+")
