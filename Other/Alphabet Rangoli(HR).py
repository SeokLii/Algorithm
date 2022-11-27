def print_rangoli(size):
    Default = 97
    Count = 0
    Line = size * 2 - 1
    Length = (size - 1) * 2
    for i in range(Line):
        SortList = []
        End_Alphabet = Default + size

        if i == 0 or i == Line - 1:
            print(chr(End_Alphabet - 1).rjust(Length + 1, '-') + ''.ljust(Length, '-'))

        elif i <= (Line - 1) // 2:
            for j in range(i + 1):
                End_Alphabet -= 1
                SortList.append(chr(End_Alphabet))
            for j in range(i):
                End_Alphabet += 1
                SortList.append(chr(End_Alphabet))

            NewWord = '-'.join(SortList)
            print(NewWord.rjust(Length + len(NewWord) - (2 * i), '-') + ''.ljust(Length - (2 * i), '-'))

        else:
            Start_number = i - size + 1
            Standard_Alphabet = Default + Start_number
            for j in range(size - Start_number):
                End_Alphabet -= 1
                SortList.append(chr(End_Alphabet))
            for j in range(size - Start_number - 1):
                End_Alphabet += 1
                SortList.append(chr(End_Alphabet))

            NewWord = '-'.join(SortList)
            print(NewWord.rjust(Start_number * 2 + len(NewWord), '-') + ''.ljust(Start_number * 2, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)