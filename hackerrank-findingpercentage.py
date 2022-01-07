if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    for student in student_marks:
        if query_name in student:
            avg_mark = sum(student_marks[student])/len(student_marks[student])
            print("{:.2f}".format(avg_mark))