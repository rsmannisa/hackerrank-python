if __name__ == '__main__':
    records = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())

        students = [name,score]
        records.append(students)

    sorted_records = sorted(records, key = lambda x: x[1])
    sec_low=0
    names=list()
    for i in range(0,len(sorted_records)):
        if sec_low == 0 and sorted_records[i][1] != sorted_records[i+1][1] :
            sec_low = sorted_records[i+1][1]
        elif sorted_records[i][1] == sec_low :
            names.append(sorted_records[i][0])
    names.sort(reverse=False)

    for s in names:
        print(s)
