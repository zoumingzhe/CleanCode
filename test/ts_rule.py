import sys
sys.path.append(r'..\CleanCode\CleanCode')
import rule


rule = rule.rule()
rule.version(isShow = True)

rule.analyse(r'.\case\rule0001.ini')
input("按回车（Enter）继续")
