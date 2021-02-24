import sys
N = int(sys.stdin.readline())
GradeList = list(map(int, sys.stdin.readline().split()))

MaxGrade = max(GradeList)
SumGrade = 0

for Grade in GradeList:
    SumGrade += Grade/MaxGrade*100

print(SumGrade/N)

