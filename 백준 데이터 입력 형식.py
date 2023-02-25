# 하나의 변수 입력
# str 형
x = input() # 기본적으로 str 형식으로 입력됨
# int 형
y = int(input())

print(x, type(x), y, type(y)) # 1 <class 'str'> 2 <class 'int'>

# 여러 개의 변수 입력
# str 형
N, M = input().split() # str 형식으로 입력되어서 int 로 입력 받기 위해서는 map 사용해야함
# int 형
L, O = map(int, input().split()) # int(input().split())은 여러 개를 입력 받을 수 없음

print(N, M, L, O) # a b 3 4

# 리스트 형 입력
arr1 = map(int, input().split()) # 리스트 형 변환 없이 하나의 변수에 2가지 이상의 값을 저장하게 되면 map 타입으로 저장됨

# 하나의 변수에 여러 값을 넣으려면 list 형식으로 넣어서 사용해야 함
# str 형
arr2 = list(input().split()) # list() 변환 안해줘도 split() 사용하면 리스트로 변환됨
# int 형
arr3 = list(map(int, input().split())) # map 사용할 때 만 list() 형 변환 필요 == 숫자 형 받을 때만 list 처리 필요
arr4 = [list(map(int, input().split())) for _ in range(L)] # 이중 리스트로 받을 수 있음

print(arr1) # <map object at 0x000001FF1FD6B940>
print(arr2) # ['a', 'b']
print(arr3) # [7, 8]
print(arr4) # [[9, 10], [11, 12], [13, 14]]

# 빠른 입력
import sys
# 하나의 변수 입력
# str 형
a = sys.stdin.readline() # 기본적으로 str 형식으로 입력됨
b = sys.stdin.readline().rstrip() # 개행 문자(줄바꿈)가 같이 입력되기 때문에 rstrip()으로 없애줘야함

print(a, b, type(b)) #a\n b <class 'str'>
# int 형
c = int(sys.stdin.readline()) # 숫자는 개행 문자 없이 입력되어 rstrip()이 필요 없음
d = int(sys.stdin.readline().rstrip())

print(c, d, type(d)) # 1 2 <class 'int'>
# 여러 개의 변수 입력
# str 형
e, f = sys.stdin.readline().split() # split()을 사용하면 개행 문자가 입력되지 않음
g, h = sys.stdin.readline().split(' ') # split(' ') 를 사용하면 띄어쓰기 빼고 개행 문자는 받아와져서 개행 문자는 입력됨
# int 형
i, j = map(int, sys.stdin.readline().split())

print(e, f) # c d
print(g, h) # e f\n
print(i, j) # 3 4

# 리스트 형 입력
srr1 = map(int, sys.stdin.readline())

# 하나의 변수에 여러 값을 넣으려면 list 형식으로 넣어서 사용해야 함
# str 형
srr2 = list(sys.stdin.readline().split()) # 개행 문자 X, but split(' ') 사용하면 개행 문자 들어옴
# int 형
srr3 = list(map(int, sys.stdin.readline().split()))
srr4 = [list(map(int, sys.stdin.readline().split())) for _ in range(2)] # 이중 리스트로 받을 수 있음
print(srr1) # <map object at 0x00000190A406FFD0>
print(srr2) # ['a', 'b']
print(srr3) # [3, 4]
print(srr4) # [[5, 6], [7, 8]]


# 결론
# 빠르게 입력하고 싶다면 sys 사용하면 되고, 여러 변수를 받을 때는 split을 쓰고, 숫자 형식 변환 할 때만 map과 list 형 변환 사용
# sys는 하나의 문자열 변수를 저장 받을 때 개행이 있기 때문에 rstrip()을 이용하면 되고, 그 외에는 rstrip() 사용할 필요가 없다

# 입력 데이터
"""
1
2
a b
3 4
5 6
a b
7 8
9 10
11 12
13 14
1
2
3 4
5 6

a
b
1
2
c d
e f
3 4
1 2
a b
3 4
5 6
7 8

"""