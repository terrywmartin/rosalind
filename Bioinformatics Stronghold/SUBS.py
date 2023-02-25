
input_file = "rosalind_subs.txt"

file = open(input_file, "r")

str1 = file.readline().strip('\n')
str2 = file.readline().strip('\n')

index = 0
output = ""
index = str1.find(str2)
while index != -1:
    output += str(index+1) + ' '
    index = str1.find(str2,index + 1)

print(output)