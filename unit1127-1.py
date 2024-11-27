import random as r

"""
for i in range(0,10):
    print(r.random(),end=" ")
for i in range(0,6):
    print(r.randint(1,49),end="  ")
"""
color ="紅橙黃綠藍靛紫"
print (color)
print("會重複的")
for i in range(0,4):
    print(r.choice(color),end="  ")

print("不會重複的")
for i in range(0,4):
    print(r.sample(color,7),end="  ")
print(type(r.sample(color,7))) 
