def count_substring(string, sub_string):
    count=0
    comp = str()
    for i in range(0, len(string)):
        for j in range(0, len(sub_string)):
            if i+j < len(string):
                comp = comp+string[i+j]
        if comp == sub_string :
            count = count+1
            comp = str()
        else:
            comp = str()
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)