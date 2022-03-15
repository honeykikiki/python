# 집합

my_set = {1,2,3,3,3}
print(my_set)

java = {"a", 'b', 'c'}
py = set(["q", 'w', 'c'])

# 교집합
print(java&py) 
print(java.intersection(py))

# 합집합
print(java | py)
print(java.union(py))

# 교집합
print(java - py)
print(java.difference(py))

#py 할줄 아는사람이 증가
py.add('t')
print(py)

# java 까먹음
py.remove('c')
print(py)
