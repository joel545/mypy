#重複式流程控制

count=1

while count<=10:
    print("NO ", count, "  Time")
    count +=1   #count=count+1

print("\n----------------------------")

while count>=1:
    print("NO ", count, "  Time")
    count -=1   #count=count-1


print("\n--------for ... range(end)------------")
for i in range(10): #0~9
    print(i)


print("\n--------for ... range(start,end)------------")
for i in range(1,10): #1~9
    print(i)

print("\n--------for ... range(起,訖,等差值)------------")
for i in range(0,10,3): #0,3,6,9
    print(i)


print("\n--------for ... range(起,訖,等差值)....else---------")
for i in range(0,10,3): #0,3,6,9
    print(i)
else:
    print("~~~~己經完成囉!!~~~~~")

print("\n--------nest loop---------------")
k=0 #記錄乘積
for i in range(1,10):   #outer
    for j in range(1,10):  #inner
        k=i*j
        print("%d X %d =%2d"%(i,j,k),end=" ")
    print()