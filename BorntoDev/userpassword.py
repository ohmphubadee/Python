def new_func():
    name = input('name : ')
    passw = input('password : ')
    namelo = input('name(login) : ')
    passwlo = input('password(login) : ')
    while name != namelo or passw != passwlo:
        print('ERROR')
        namelo = input("name : ")
        passwlo = input('password(login) : ')
    print('SUCCESS')

new_func()