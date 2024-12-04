price1 = 35
price2 =50  
if price1 < price2:
    print("price1小於price2" )
else:
    print("price1大於price2" )
    
spendtime = int (input("輸入你的靈修時間(分鐘)："))

print ((spendtime) , "分鐘")

print("\n-----------------------")

#count=1
#while count< 20:
#     print ("*")

for i in range(1,10):
    for j in range(1,10): 
        k=i*j
        print("%d * %d = %2d" %(i,j,k),end=" ")
    print()
