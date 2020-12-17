with open("sample_10.txt", "r") as fp:
    lines = [int(line.rstrip()) for line in fp.readlines()]

one_jolt = 0
two_jolt = 0
three_jolt = 0 
outlet_rating = 0
lines.append(max(lines)+3) # because max jolt is added


while True:
    #print(1 in lines)
    if (outlet_rating + 1) in lines:
        one_jolt+=1
        outlet_rating += 1
    elif outlet_rating+2 in lines:
        two_jolt+=1
    elif (outlet_rating + 3) in lines:
        three_jolt += 1
        outlet_rating+=3
    else:
        break

    

# part 2
sol = {0:1}
for line in sorted(lines):
    sol[line] = 0
    if line - 1 in sol:
        sol[line]+=sol[line-1]
    if line - 2 in sol:
        sol[line]+=sol[line-2]
    if line - 3 in sol:
        sol[line]+=sol[line-3]

print(sol)
print(sol[max(lines)])

