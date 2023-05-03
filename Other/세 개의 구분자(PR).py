def solution(myStr):
    return ['EMPTY'] if len(myStr.replace('a', ' ').replace('b',' ').replace('c',' ').split()) == 0 else myStr.replace('a', ' ').replace('b',' ').replace('c',' ').split()