if __name__ == '__main__':
    n = input()
    n = int(n)

    if n < 1 or n > 150:
        n = input("Please input number between 1 and 150: ")
        n = int(n)

    number = str()
    for i in range(1,n+1):
        number = number+str(i)
    
    print(number)