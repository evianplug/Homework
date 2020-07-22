file = open('text.txt')
i = print(file.readline())
FB = []
while True:
    entry = ''
    if i % 2 == 0:
        entry += "F"
    if i % 5 == 0:
        entry += "B"
    if i % 2 != 0 and i % 5 != 0:
        entry = i

    FB.append(entry)

for i in FB:
    print(i)
