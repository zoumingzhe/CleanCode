#!/usr/bin/env python3
# coding=utf-8
# ----------------------------------------------------------------------------------------------------
# 类 scan
# ----------------------------------------------------------------------------------------------------
# 变更履历：
# 2020-06-22 | Zou Mingzhe   | Ver0.1  | 初始版本
# ----------------------------------------------------------------------------------------------------
# MAP：
# 已测试 | version(self, ...)           | 版本显示
# ----------------------------------------------------------------------------------------------------
import ztools.file.filebase as filebase
# ----------------------------------------------------------------------------------------------------
class scan:
    """
    scan类提供扫描器支持。
    """
    def __init__(self):
        self.__version = "0.1"
        self.__path = {}
# ----------------------------------------------------------------------------------------------------
    def version(self, isShow = False):
        """
        版本显示：
        输入参数：isShow = False
        返回参数：self.__version
        说明：调用该方法将返回类的版本号，若isShow == True则会在屏幕上打印版本号。
        """
        if(isShow):
            print("[CleanCode]-[scan]-[vesion:%s]" % self.__version)
        return self.__version
# ----------------------------------------------------------------------------------------------------
    def scan(self, directory):
        """
        扫描文件：
        输入参数：directory, sub=False, prefix=None, postfix=None
        返回参数：info
        说明：该方法在指定目录（directory）下进行文件扫描，
        参数sub指定是否对子目录扫描（默认不扫描），
        参数prefix、postfix分别指定文件名的前缀和后缀。
        """
        return filebase.scan(self, directory, sub=True, prefix=None, postfix=None)
# ----------------------------------------------------------------------------------------------------