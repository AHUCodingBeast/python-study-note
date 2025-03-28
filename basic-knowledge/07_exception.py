import sys


def demo1():
    try:
        x = int(input("请输入一个数字: "))
        print("您输入的数字是:", x)
    except ValueError:
        print("您输入的不是数字，请再次尝试输入！")


def demo2():
    try:
        f = open('../notebook/MarkDown语法笔记.txt', 'r',encoding='utf-8')
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
        raise Exception('Could not convert data to an integer. {}'.format(s))
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    else:
        # 没有发生错误时执行
        print("No errors occurred. finished successfully.")
    finally:
        print("文件已关闭")
        f.close()


if __name__ == '__main__':
    demo2()