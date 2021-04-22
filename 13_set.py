# s_from_list = set([1,2,3,4])
# print(s_from_list)

s = set()
s.add(1)
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(1.4)
s1 = s.union({1,2,3,4,5,6})
s2 = s.intersection({1,2,3,4,5})

print(s)
print(s1)
print(s2)

# set function
s.remove(1)
print(s) 