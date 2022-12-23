s=input()

for i in range(len(s)):
    if s[i:]==s[i:][::-1]:
        print(len(s)+i)
        break


# 잘못한 풀이
# 문자열의 뒤쪽부터 문자열을 인덱싱하여 리버스한 값이 있는지 찾는다
n = input()
listn = list(n)
sub = n[-1]

max = len(n) -1
for i in range(len(listn)-2, len(listn)//2-1, -1):
    sub += n[i]
    if sub == n[i-len(sub)+1:i+1]:
        max = len(n[:i-len(sub)+1])
    elif sub == n[i-len(sub):i]:
        max = len(n[:i - len(sub)])
    elif sub == n[i-len(sub)-1:i-1]:
        max = len(n[:i - len(sub) - 1])
print(n[i-len(sub)+1:i+1], n[i-len(sub):i], n[i-len(sub)-1:i-1], sub)
print(len(n) + max)

n = input()

if len(n) <= 1:
    print(len(n))
else:
    listn = list(n)
    sub = n[-1]

    max = len(n) -1
    for i in range(len(listn)-2, len(listn)//2-1, -1):
        sub += n[i]

        if len(n[:i+1]) + 2 > len(sub):
            if sub == n[i - len(sub) + 1:i + 1]:
                max = len(n[:i - len(sub) + 1])
            elif sub == n[i - len(sub):i]:
                max = len(n[:i - len(sub)])
            elif sub == n[i - len(sub) - 1:i - 1]:
                max = len(n[:i - len(sub) - 1])
        elif len(n[:i+1]) + 1 == len(sub):
            if sub == n[i - len(sub) + 1:i + 1]:
                max = len(n[:i - len(sub) + 1])
            elif sub == n[i - len(sub):i]:
                max = len(n[:i - len(sub)])
        else:
            if sub == n[i - len(sub) + 1:i + 1]:
                max = len(n[:i - len(sub) + 1])
    print(len(n) + max)