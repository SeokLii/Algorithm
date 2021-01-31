#범위 500 : N3 알고리즘 = 1초
#범위 2,000 : n2 알고리즘 = 1초
#범위 100,000 : NlogN 알고리즘 = 1초
#범위 10,000,000 : N 알고리즘 = 1초

dwarf_height = [int(input()) for _ in range(9)]
dwarf_height.sort()
height_sum = sum(dwarf_height)
BP = True

for i in range(8):
    for j in range(i+1, 9):
        if height_sum - (dwarf_height[i] + dwarf_height[j]) == 100:
            A = dwarf_height[i] #삭제하면 위치가 바뀌므로 변수에 넣어서 삭제
            B = dwarf_height[j]
            dwarf_height.remove(A)
            dwarf_height.remove(B)
            for k in dwarf_height:
                print(k)
            BP = False
            break

    if BP == False:
        break