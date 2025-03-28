#!/usr/bin/python3

import os
import os.path

# path = 'D:/UC/'
ls = []

# 使用 with 语句确保文件能够正确关闭，即使发生异常也能保证资源释放 有点类似Java的 try with resources
try:
    with open('../notebook/MarkDown语法笔记.txt', 'r', encoding='utf-8') as f:
        # 打印文件内容
        print(f.read())
        # 读取文件第一行
        # print(f.readline(10))
except FileNotFoundError:
    # 文件不存在时的异常处理
    print("指定路径下的文件不存在")
except IOError as e:
    # 其他输入输出相关的异常处理
    print(f"读取文件时发生错误: {e}")


def getAppointFile(path, ls):
    fileList = os.listdir(path)
    try:
        for tmp in fileList:
            pathTmp = os.path.join(path, tmp)
            if os.path.isdir(pathTmp):
                getAppointFile(pathTmp, ls)
            elif pathTmp[pathTmp.rfind('.') + 1:].upper() == 'PY':
                ls.append(pathTmp)
    except PermissionError:
        pass


def main():
    while True:
        path = input('请输入路径:').strip()
        if os.path.isdir(path):
            break

    getAppointFile(path, ls)
    # print(len(ls))
    print(ls)
    print(len(ls))
