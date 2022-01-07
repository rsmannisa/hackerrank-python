if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    test = list(arr)
    test.sort(reverse=True)

    print(test)
    i=0
    while i<n:
        if test[i] != test[i+1]:
            print(test[i+1])
            break
        i=i+1