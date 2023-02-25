
startnum = 4616
endnum = 9004

total = sum([ x if x%2 != 0 else 0 for x in range(startnum,endnum+1)])

print(total)