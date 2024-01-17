opCodes = { 'NOP':'0',  'BNK':'1',  'OUT':'2',  'CLC':'3',  'SEC':'4',  'LSL':'5',  'ROL':'6',  'LSR':'7',
            'ROR':'8',  'ASR':'9',  'INP':'10', 'NEG':'11', 'INC':'12', 'DEC':'13', 'LDI':'14', 'ADI':'15',
            'SBI':'16', 'CPI':'17', 'ACI':'18', 'SCI':'19', 'JPA':'20', 'LDA':'21', 'STA':'22', 'ADA':'23',
            'SBA':'24', 'CPA':'25', 'ACA':'26', 'SCA':'27', 'JPR':'28', 'LDR':'29', 'STR':'30', 'ADR':'31',
            'SBR':'32', 'CPR':'33', 'ACR':'34', 'SCR':'35', 'CLB':'36', 'NEB':'37', 'INB':'38', 'DEB':'39',
            'ADB':'40', 'SBB':'41', 'ACB':'42', 'SCB':'43', 'CLW':'44', 'NEW':'45', 'INW':'46', 'DEW':'47',
            'ADW':'48', 'SBW':'49', 'ACW':'50', 'SCW':'51', 'LDS':'52', 'STS':'53', 'PHS':'54', 'PLS':'55',
            'JPS':'56', 'RTS':'57', 'BNE':'58', 'BEQ':'59', 'BCC':'60', 'BCS':'61', 'BPL':'62', 'BMI':'63'  }

lines, lineinfo, lineadr, labels = [], [], [], {}
LINEINFO_NONE, LINEINFO_ORG, LINEINFO_BEGIN, LINEINFO_END	= 0x00000, 0x10000, 0x20000, 0x40000

import sys
if len(sys.argv) < 2: print('USAGE: asm.py <sourcefile> [-s[<tag>]]'); exit(1)

try: f = open(sys.argv[1], 'r')
except: print("ERROR: Can't find file \'" + sys.argv[1] + "\'."); exit(1)
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
            for c in lines[i][k+1:l]: replaced += str(ord(c)) + ' '
            lines[i] = lines[i][0:k] + replaced + lines[i][l+1:]
        else: break

    if (lines[i].find(';') != -1): lines[i] = lines[i][0:lines[i].find(';')]
    lines[i] = lines[i].replace(',', ' ')

    lineinfo.append(LINEINFO_NONE)
    if lines[i].find('#begin') != -1:
        lineinfo[i] |= LINEINFO_BEGIN
        lines[i] = lines[i].replace('#begin', '')
    if lines[i].find('#end') != -1:
        lineinfo[i] |= LINEINFO_END
        lines[i] = lines[i].replace('#end', '')
    k = lines[i].find('#org')
    if (k != -1):
        s = lines[i][k:].split(); rest = ""
        lineinfo[i] |= LINEINFO_ORG + int(s[1], 0)
        for el in s[2:]: rest += " " + el
        lines[i] = (lines[i][0:k] + rest).strip()

    if lines[i].find(':') != -1:
        labels[lines[i][:lines[i].find(':')]] = i
        lines[i] = lines[i][lines[i].find(':')+1:]

    lines[i] = lines[i].split()

    for j in range(len(lines[i])-1, -1, -1):
        try: lines[i][j] = opCodes[lines[i][j]]
        except:
            if lines[i][j].find('0x') == 0 and len(lines[i][j]) > 4:
                val = int(lines[i][j], 16)
                lines[i][j] = str(val & 0xff)
                lines[i].insert(j+1, str((val>>8) & 0xff))

adr = 0
for i in range(len(lines)):
    for j in range(len(lines[i])-1, -1, -1):
        e = lines[i][j]
        if e[0] == '<' or e[0] == '>' : continue
        if e.find('+') != -1: e = e[0:e.find('+')]
        if e.find('-') != -1: e = e[0:e.find('-')]
        try:
            labels[e]; lines[i].insert(j+1, '0x@@')
        except: pass
    if lineinfo[i] & LINEINFO_ORG: adr = lineinfo[i] & 0xffff
    lineadr.append(adr);
    adr += len(lines[i])

for l in labels: labels[l] = lineadr[labels[l]]

for i in range(len(lines)):
    for j in range(len(lines[i])):
        e = lines[i][j]; pre = ''; off = 0
        if e[0] == '<' or e[0] == '>': pre = e[0]; e = e[1:]
        if e.find('+') != -1: off += int(e[e.find('+')+1:], 0); e = e[0:e.find('+')]
        if e.find('-') != -1: off -= int(e[e.find('-')+1:], 0); e = e[0:e.find('-')]
        try:
            adr = labels[e] + off
            if pre == '<': lines[i][j] = str(adr & 0xff)
            elif pre == '>': lines[i][j] = str((adr>>8) & 0xff)
            else: lines[i][j] = str(adr & 0xff); lines[i][j+1] = str((adr>>8) & 0xff)
        except: pass
        try: int(lines[i][j], 0)
        except: print('ERROR in line ' + str(i+1) + ': Undefined expression \'' + lines[i][j] + '\''); exit(1)

insert = ''; showout = True
for i in range(len(lines)):
    if lineinfo[i] & LINEINFO_BEGIN: showout = True
    if lineinfo[i] & LINEINFO_END: showout = False
    if showout:
        if lineinfo[i] & LINEINFO_ORG:
            if insert: print(':' + insert); insert = ''
            print('%04.4x' % (lineinfo[i] & 0xffff))
        for e in lines[i]:
            insert += ('%02.2x' % (int(e, 0) & 0xff)) + ' '
            if len(insert) >= 16*3 - 1: print(':' + insert); insert = ''
if insert: print(':' + insert)

if len(sys.argv) > 2:
    k = sys.argv[2].find('-s')
    if k != -1:
        sym = sys.argv[2][k+2:]
        for key, value in labels.items():
            if key.find(sym) != -1:
                print('#org '+ '%04.4x' % (value & 0xffff) + '\t' + key + ':')
