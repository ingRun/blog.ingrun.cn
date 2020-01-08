import os
k = "999"

while k is not '0':
    if k == '1':
        os.system('python3 a.py && python3 c.py && python3 b.py')
    elif k == '2':
        os.system('python3 a.py')
    elif k == '3':
        os.system('python3 c.py && python3 b.py')
    elif k == '4':
        os.system('python3 b.py')
    elif k == '5':
        os.system('python3 c.py')
    print('1:  同步远程仓库， 并重启项目！')
    print('2:  仅同步远程仓库')
    print('3:  重启项目')
    print('4:  运行项目')
    print('5:  关闭项目')
    print('0:  退出')
    print()
    k = input('请选择：')

