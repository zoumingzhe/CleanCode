import sys
sys.path.append(r'..\CleanCode\CleanCode')
import clean
import scan as s


sc = s.scan()
sc.version(isShow = True)

list = sc.scan(r'.\case', sub=True, prefix=None, postfix=None)
print(list)
input("按回车（Enter）继续")
