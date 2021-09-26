#Jordan Walker CSC110 The code create a center version of lab and rab using twoinput instead of one
code = str(input("Enter bar string:\n"))
print("+------------------+")
i = 0
while i<len(code):
   print("|" + " " * (9-int(code[i])) + "#" * int(code[i]) + "#" * int(code[i+1]), end="")
   print(" " * (9-int(code[i+1])) + "|")
   i = i +2
print("+------------------+")
