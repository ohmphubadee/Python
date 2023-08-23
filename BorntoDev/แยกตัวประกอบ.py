number = int(input(""))
list = []
con = True
while con and number != 2: 
    for i in range(2,number,1): 
        con = False
        if number%i == 0 and number != 2:
            list.append(i)
            number = int(number/i)
            con = True
            break
list.append(number)
dic = {}
countdic = 0
for i in list:
    dic[str(i)] = list.count(i)
for x, y in dic.items():
    countdic += 1
    if countdic == len(dic):
        if y == 1:
            print(f'{int(x)}')
        else:
            print(f'{int(x)}^{y}')
    else:
        if y == 1:
            print(f'{int(x)}',end=" * ")
        else:
            print(f'{int(x)}^{y}',end=" * ")