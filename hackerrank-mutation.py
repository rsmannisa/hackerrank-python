def mutate_string(string, position, character):
    stringlist = list(string)
    stringlist[position] = character
    string = "".join(stringlist)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)