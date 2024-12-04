#dict 字典 容器
#元素以「key (鍵)」,「value(值)」配對的方式儲存
#字串、整數與浮點數...等可以為「鍵」
#以{} 括住
#key:value

coffee={
    "arabica":500,
    "robusta":450,
    "liberia":470
}

print(coffee)
print(type(coffee))

print("coffee 所有的鍵：",coffee.keys())    #取得鍵,使用keys() 函數
print("robusta的價格：", coffee.get('robusta'),'元')    #get() 取回鍵的值

print('\n-------走訪dict-------------------')
for e in coffee:
    print("%-10s\t-->\t%3d元"%(e,coffee.get(e)))