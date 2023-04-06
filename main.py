from os import system, name

def clear():

    # clear Windows terminal/shell
    if name == 'nt':
        _ = system('cls')

    # mac and linux
    else:
        _ = system('clear')

