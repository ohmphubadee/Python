base = int(input())
height = int(input())
area = base*height/2
if area.is_integer():
    print(f'{int(area)} cm2')
else:
    print(f'{area:.1f} cm2')

