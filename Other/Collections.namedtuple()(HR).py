from collections import namedtuple

N = int(input())
student = namedtuple('student', input().split())
Marks = 0

for _ in range(N):
    students = student._make(input().split())
    Marks += int(students.MARKS)

print(round(Marks / N, 2))
