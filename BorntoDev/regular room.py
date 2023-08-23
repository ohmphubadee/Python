number = int(input())

def print_0(number):
    for i in range(2*number+1):
        print("0",end="")
    print("\n",end="")

def pri_top(x,y):
    for i in range(y):
        if i<x+1:
            print(i,end="")
        else:
            print(x+1,end="")
    for i in range(y,-1,-1):
        if i>x+1:
            print(x+1,end="")
        else:
            print(i,end="")
    print("\n",end="")

def pri_bot(x,y): #x=number,y=number
    for i in range(y):
        if i < x:
            print(i,end="")
        else:
            print(x-1,end="")
    for i in range(y,-1,-1):
        if i < x:
            print(i,end="")
        else:
            print(x-1,end="")
    print("\n",end="")

print_0(number)
for i in range(0,number):
    pri_top(i,number)   
for i in range(number,1,-1):
    pri_bot(i,number)
print_0(number)


