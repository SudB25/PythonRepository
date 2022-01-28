# f = open("sample.txt", "w")
# f.write("Testing")
# f.close()


# f = open("sample.txt", "a")
# f.write("\nappending new file")
# f.close()

# <-- Extracring required data from file-->
import re


# if re.match("(.*)@(.*).(.*)", strEmail):

f = open("sample.txt", "r")
s = f.read()

# ans = re.match("[0-9]*",s)
# ans = re.match("[a-zA-Z]*",s)

# ans = re.findall("[0-9]+-[0-9]+-[0-9]+",s)
ans = re.findall("[A-Z][a-z]+ [A-Z][a-z]+ ",s)

print(ans)

# print(f.readlines())
# f.close()
