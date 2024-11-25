file = 'test_1-3.output'

with open(file, 'r') as file:
    messages = file.readlines()

firstHint = []
secondHint = []
thirdHint = []

for full in messages:
    pref, line = full.split('\t')
    line = line.split('2')
    firstHint.append(str(pref) + str(line[0]))
    if len(line) > 1:
        second = line[1].split('3')
        secondHint.append(second[0])
        if len(second) > 1:
            thirdHint.append(second[1])

with open('FirstHints', 'w') as file:
    for line in firstHint:
        file.write(line + '\n')

with open('SecondHints', 'w') as file:
    for line in secondHint:
        file.write(line + '\n')

with open('ThirdHints', 'w') as file:
    for line in thirdHint:
        file.write(line + '\n')

print(firstHint)
print(len(firstHint))
print(secondHint)
print(len(secondHint))
print(thirdHint)
print(len(thirdHint))