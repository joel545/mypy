"""
例外
Exception

"""
import os
# os.mkdir("myfolder")
try:
    os.rmdir("myfolder")
    print("my folder 已刪除")
except:
    print("找不到myfolder資料夾")
i=10
print(f'i={i}')
try :
    print(f'j={j}')
except:
    print('')