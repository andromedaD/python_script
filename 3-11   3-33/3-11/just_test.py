list1=['dsda','sdas','dsad','fghfgh']
list2=[1,31,3123,432,768]

dict1={'name':'wangzhiben','sex':'man','city':'Nanjing'}

import json
dict2=json.dumps(dict1)
print(dict2)
print(type(dict2))
print(type(dict1))


print(type(list1))

json.dump(dict1,open('db','w'))
print(json.load(open('db','r')))

