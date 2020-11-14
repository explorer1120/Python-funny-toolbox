# Funny-toolbox by Explorer1120
#：py.exe main.py
from os import *
import time
import random as rand

rand.seed(time.time())

# data
_plugin_list_name = ['随机数生成器', '随机字母生成器', '计算器', '计算圆周率']
_plugin_list_english = ['random', 'random_abc', 'calc', 'pi']
_end_number = [3]
wait = 0.5


# func
def clear():
    system('cls')


def pause():
    system("pause")


# plugins
def random():
    _min = int(input('请输入最小值:'))
    _max = int(input('请输入最大值:'))
    print('为您生成的随机数:', rand.randint(_min, _max))


def random_abc():
    n = int(input('请输入生成随机字母的数量:'))
    for i in range(n):
        print(chr(97 + rand.randint(0, 25)), end='')
    print('\n', end='')


def calc():
    a = input('请输入算式:')
    eval(a)


# else
def openplu(name, cho):
    clear()
    print('****' + '正在运行插件:', _plugin_list_name[cho] + '****')
    eval(name + '()')


# main
print('loading...')
time.sleep(wait)

while (True):
    clear()
    print('********欢迎使用滑稽工具箱********')
    print('* 1. 数学类工具')
    print('* 2. 系统类工具')
    print('* 3. 编程类工具')
    print('* 4. 其他工具')
    print('* 5. 设置')
    cho = input('请选择您想要进入的分区: ')

    if cho == '1':  # 数学类
        clear()
        print('******数学类工具列表******')
        for i in range(0, (_end_number[0]) + 1):
            print('*', str(i - 0 + 1) + '.', _plugin_list_name[i])
        cho = int(input('请选择您想要打开的插件: '))
        openplu(_plugin_list_english[cho + 0 - 1], cho)
    pause()
