
filename = "GC_input.txt"

f = open(filename, "r")


input_dict = {}
str1 = ""
total_C =0
total_G = 0
id = ""
max_avg = 0
max_id = ""
for line in f:
    if line[0] == ">":
        if id == "":
            id = line.strip('\n')
        else:
            input_dict[id] = str1
            str1 = ""
            id = line.strip('\n')
    else:
        str1 += line.strip('\n')

input_dict[id] = str1
for id in input_dict:
    total = ( ( input_dict[id].count("C") + input_dict[id].count("G") ) / len(input_dict[id]) ) *100
    if total > max_avg:
        max_avg = total
        max_id = id


print(max_avg)
print(max_id)