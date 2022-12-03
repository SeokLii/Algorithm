# 36.Collections.namedtuple()
# > from collections import namedtuple
# > 이름을 가진 tuple로서 객체처럼 사용이 가능
# > Point1 = namedtuple('Point', ['x', 'y'], rename=True)
# > 첫번째 인자는 tuple 이름이고, 두번째부터 값 선언, 안에 리스트 콤마('x, y') 및 띄어쓰기('x y')로 구분 선언 가능
# > rename 인자는 에약어나 중복되는 값을 사용할 수 있도록 해줌