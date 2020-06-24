import sys
sys.path.append(r'..\CleanCode\CleanCode')
import scan as s


sc = s.scan()
sc.version(isShow = True)

list = sc.scan(r'.\case', sub=True, prefix=None, postfix=(".h",".cpp"))
print(list)
input("按回车（Enter）继续")
