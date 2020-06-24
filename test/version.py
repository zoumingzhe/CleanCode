import sys
sys.path.append(r'..\CleanCode\CleanCode')
import clean
import rule
import scan


clean = clean.clean()
clean.version(isShow = True)
input("按回车（Enter）继续")

rule = rule.rule()
rule.version(isShow = True)
input("按回车（Enter）继续")

scan = scan.scan()
scan.version(isShow = True)
input("按回车（Enter）继续")
