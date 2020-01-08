import os
k = "999"

while k is not '0':
    if k == '1':
        os.system('python3 a.py')
        os.system('c.py')
        cmd = 'python3 b1.py && python3 b2.py && python3 b2.py && '
        os.system(cmd)
    elif k == '2':
        os.system('python3 a.py')
    elif k == '3':
        os.system('c.py')
        cmd = 'python3 b1.py && python3 b2.py && python3 b2.py && '
        os.system(cmd)
    elif k == '4':
        cmd = 'python3 b1.py && python3 b2.py && python3 b2.py && '
        os.system(cmd)
    else:
        print('1:  同步远程仓库， 并重启项目！')
        print('2:  仅同步远程仓库')
        print('3:  重启项目')
        print('4:  运行项目')
        print('0:  退出')
        print()
        k = input('请选择：')

