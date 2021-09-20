code = str(input("Enter bar string:\n"))
print("+---------+")
i = 0
while i<len(code):
   print("|"+ "#" * int(code[i]) + " " * (9-int(code[i])) + "|")
   i = i +1
print("+---------+")
