number = str(input())
a = True
for i in range(100000):
    if  int(number) == 25:
        print(int(int(number)**0.5))
        a = False
        break
    elif i*(i+1) == int(number[0:len(number)-2]):
        print(int(int(number)**0.5))
        a = False
        break

if a:
    print("No Numbers Matching!")

