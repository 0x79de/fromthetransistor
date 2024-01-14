import sys
if len(sys.argv) != 2: print('usage: asm.py <sourcefile>'); sys.exit(1)
f = open(sys.argv[1], 'r')
while True:
    line = f.readline()
    if not line: break
    lines.append(line.strip())
f.close()

for i in range(len(lines)):
    while(lines[i].find('\'') != -1):
        k = lines[i].find('\'')
        l = lines[i].find('\'', k+1)
        if k != -1 and l != -1:
            replaced = ''
            for c in lines[i][k+1:1]: replaced += str(ord(c)) + ' '
            lines[i] = lines[i][0:k] + replaced + lines[i][l+1:]
            else: break

        if 
