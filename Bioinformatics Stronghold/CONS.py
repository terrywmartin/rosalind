
input_file = "rosalind_cons.txt"

input_matrix = []
id_matrix = []
file = open(input_file,"r")
str1 = ""
for line in file:
    if line[0] == '>':
        if str1 != "":
            input_matrix.append(str1.strip('\n'))
            str1 = ""
    else:
        str1 += line.strip('\n')
if str1 != "":
    input_matrix.append(str1.strip('\n'))
file.close()

n = len(input_matrix[0])
#profile_matrix = [ [0] * n for i in range(4)]

consensus_dict = {"A": [0] * n,
                  "C": [0] * n,
                  "G": [0] * n,
                  "T": [0] * n}


for i in range(len(input_matrix)):
    for j in range(len(input_matrix[i])):
        consensus_dict[input_matrix[i][j]][j] += 1

output_file = "cons_output.txt"
outfile = open(output_file,"w")
output = ""
for i in range(len(input_matrix[0])):
    largest = -1
    index = ""
    for key in consensus_dict:
        if consensus_dict[key][i] > largest:
            largest = consensus_dict[key][i]
            index = key
    output += index
    
print(output)
outfile.write(output + '\n')
for key in consensus_dict:
    output = f"{key}: "
    for item in consensus_dict[key]:
        output += str(item) + ' '
    print(output)
    outfile.write(output + '\n')

outfile.close()

