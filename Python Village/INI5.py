
input_file = "infile1.txt"
output_file = "outfile1.txt"

file = open(input_file, "r")
fileout = open(output_file, "w")

line_count = 1
for line in file:
    if line_count%2 == 0:
        fileout.write(line)
    line_count += 1

