from calendar import c


cab = {3 : "유재석", 100 : "김태호", "a" : 3}

# print(cab[3])
# print(cab.get(3))

# print(cab.get(5)) 
# print(cab.get(5, "사용 가능")) 

# print(3 in cab)
# print(5 in cab)

# print(cab["a"])

cab["c"] = 'honey'
print(cab["c"])
cab["c"] = 'kikiki'
print(cab["c"])

del cab["a"]

print(cab)

print(cab.keys())

print(cab.values())

print(cab.items())

cab.clear()

print(cab)

