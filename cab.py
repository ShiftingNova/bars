 code = str(input("Enter bar string:"))
print("+------------------+")
i = 0
while i<len(code):
   print("|" + " " * (9-int(code[i])) + "#" * int(code[i]) + "#" * int(code[i+1]) + " " * (9-int(code[i+1])) + "|")
   i = i +2
print("+------------------+")
