if __name__ == '__main__':
    N = int(input())
    numbers = list()
    for i in range(0,N):
        cmd, *numb = input().split()
        cmd = str(cmd).lower()
        number = list(map(int, numb))

        if cmd == "insert":
            numbers.insert(number[0], number[1])
        elif cmd == "print":
            print(numbers)
        elif cmd == "remove":
            numbers.remove(number[0])
        elif cmd == "append":
            numbers.append(number[0])
        elif cmd == "sort":
            numbers.sort()
        elif cmd == "pop":
            numbers.pop()
        elif cmd == "remove":
            numbers.remove(number[0])
        elif cmd == "reverse":
            numbers.reverse()
        else:
            print("command invalid")