number = int(input())
dic = {}
for i in range(number):
    value = input()
    keys = int(input())
    dic[keys]=value
print(dic)
for i in range(number):
    print(f'Chapter {i+1}')
    print(f'{dic[i+1]}')
