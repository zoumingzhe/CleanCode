#!/usr/bin/env python3
# coding=utf-8
# ----------------------------------------------------------------------------------------------------
# 类 rule
# ----------------------------------------------------------------------------------------------------
# 变更履历：
# 2020-06-22 | Zou Mingzhe   | Ver0.1  | 初始版本
# ----------------------------------------------------------------------------------------------------
# MAP：
# 已测试 | version(self, ...)           | 版本显示
# ----------------------------------------------------------------------------------------------------
import configparser
# ----------------------------------------------------------------------------------------------------
class rule():
    """
    rule类提供规则生成器支持。
    """
    def __init__(self):
        self.__version = "0.1"
        self.__path = None
        self.__file_type = None
# ----------------------------------------------------------------------------------------------------
    def version(self, isShow = False):
        """
        版本显示：
        输入参数：isShow = False
        返回参数：self.__version
        说明：调用该方法将返回类的版本号，若isShow == True则会在屏幕上打印版本号。
        """
        if(isShow):
            print("[CleanCode]-[rule]-[vesion:%s]" % self.__version)
        return self.__version
# ----------------------------------------------------------------------------------------------------
    def analyse(self, path, encoding='utf-8'):
        """
        版本显示：
        输入参数：path 配置文件路径
        返回参数：self.__version
        说明：调用该方法将解析指定路径的配置文件。
        """
        config = configparser.ConfigParser()
        config.read(path, encoding = encoding)
        sections = config.sections()
        if 'file' in sections:
            items = config.items('file')
            dicts = dict(items)
            self.__path = dicts['path']
            if 'file_type' in dicts:
                self.__file_type = dicts['file_type']
            print(self.__path)
            print(self.__file_type)
# ----------------------------------------------------------------------------------------------------
    def get_path(self):
        """
        版本显示：
        输入参数：path 配置文件路径
        返回参数：self.__version
        说明：调用该方法将解析指定路径的配置文件。
        """
        return self.__path
# ----------------------------------------------------------------------------------------------------
