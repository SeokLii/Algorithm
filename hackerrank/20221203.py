# 36.Collections.namedtuple()
from collections import namedtuple

# namedtuple(typename, fieldname, rename=false)
# typename: 부여할 이름, fieldname: 필드 이름, rename: 유효하지 않은 필드명 사용 여부
point = namedtuple('point', ['x', 'y', 'x', 'class'], rename=True)
# fieldname에 'x, y' 또는 'x y' 처럼 콤마 또는 띄어쓰기로 구분된 하나의 문자열 사용 가능
pointvalue = point(10, 20, 30, 40)
print(pointvalue) #= Point(x=10, y=20, _2=30, _3=40)

# 메서드
# 1. _make(): 새로운 객체생성 하나의 인자만 들어가므로 값을 넣을 때는 iterable 자료형 사용
newpoint = point._make([40, 30, 20, 10])
print(newpoint) #= point(x=40, y=30, _2=20, _3=10)

# 2. _fields: 필드의 이름 확인
print(point._fields) #= ('x', 'y', '_2', '_3')

# 3. _asdict(): dict 타입으로 변환
dictpoint = newpoint._asdict()
print(dictpoint, type(dictpoint)) #= {'x': 40, 'y': 30, '_2': 20, '_3': 10} <class 'dict'>

# 4. _replace(): tuple과 동일하게 불변하기 때문에 값을 수정하지 못하므로 수정된 값(=kwargs)을 가진 새로운 객체 반환
# args(=arguments): 복수 인자 사용 가능 vs kwargs(=keyword arguments): 키워드= 특정 값
replacepoint = newpoint._replace(x=100, _2=50)
print(replacepoint) #= point(x=100, y=30, _2=50, _3=10)

# 37.Time Delta
