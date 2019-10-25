file = 'input.txt'
factor_table = []
target = None
output = ''

with open(file) as f:
    line = f.readline()
    while(line):
        if ':' in line:
            i,s = line.split(':')
            pair = (int(i), s[:-1])
            factor_table.append(pair)
        else:
            target = int(line)
        line = f.readline()

factor_table = sorted(factor_table, key=lambda x:x[0])
# print(factor_table)

for i, ele in enumerate(factor_table):
    if target % ele[0] is 0:
        output += ele[1]
print(output if output!='' else target)