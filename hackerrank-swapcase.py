def swap_case(s):
    newstring = str()
    for i in s:
        if i.islower():
            i = i.upper()
        else:
            i = i.lower()
        newstring = newstring+i
    return newstring

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)