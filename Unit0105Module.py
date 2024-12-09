import sys
import platform as pf
print("系統路徑:")
print(sys.path)
print(type(sys.path))
for s in sys.path:
    print(s)
    print("作業系統:",pf.system())
    