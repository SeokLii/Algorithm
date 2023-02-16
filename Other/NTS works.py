Base = ['LeeK', 'LeeC', 'LeeD', 'HanK', 'HanC', 'HanD']
Found = ['LeeK', 'LeeD', 'ChoiK', 'HanK', 'HanD', 'DanielKang']

## set 타입으로 변환
Base, Found = set(Base), set(Found)

## 출력
# Base 에는 없고, Found 에 있는 이름을 나열
print(Found - Base)

# Base 에는 있고, Found 에 없는 이름을 나열
print(Base - Found)