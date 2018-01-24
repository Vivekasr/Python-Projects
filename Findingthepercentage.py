n = int(input())
student_marks = {}
for _ in range(n):
        name, *line = input().split()
        scores = list(map(lambda x: float(x), line))
        student_marks[name] = scores
studname = input()        
studname_marks_lst = student_marks[studname]
tot = 0
for marks in studname_marks_lst:
        tot = tot+marks
avg = tot/3
print("%.2f" % avg)
