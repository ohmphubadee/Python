a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
if len(a) != len(b):
    print("Invalid")
else:
    for i in range(0,len(a)):
        if a[i] + b[i] > 32458:
            print('Invalid')
            break
        else:
            print(f'{a[i]+b[i]}',end=" ")
