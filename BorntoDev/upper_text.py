word = input()
newword = ''
for i in range(len(word)):
    if i%2 == 1:
        newword += word[i].upper()
    else:
        newword += word[i]
print(newword)