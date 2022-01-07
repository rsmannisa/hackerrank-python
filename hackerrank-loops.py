if __name__ == '__main__':
    n = input()
    n = int(n)

    if n < 1 or n > 20:
        n = input("insert number in range of 1 and 20: ")
        n = int(n)
        
    for i in range(0,n):
        print(i*i)
        
