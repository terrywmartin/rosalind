
input_file = "rosalind_hamm.txt"


file = open(input_file, "r")

input_string1 = file.readline().strip('\n')
input_string2 = file.readline().strip('\n')

dH = 0

for i in range(len(input_string1)):
    if input_string1[i] != input_string2[i]:
        dH += 1

print(dH)