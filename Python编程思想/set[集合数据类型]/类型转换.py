''''''
'''list->set'''
l1 = [1, 2, 3, 4]
s1 = set(l1)

'''tuple->set'''
l1 = (1, 2, 3, 4)
s1 = set(l1)

'''tuple->dict'''
l1 = {1:"asd", 2:"sdd"}
s1 = set(l1)

'''set->list'''
set = {1, 2, 3, 4}
l = list(set)
print(l)

'''set->tuple'''
set = {1, 2, 3, 4}
l = tuple(set)
print(l)