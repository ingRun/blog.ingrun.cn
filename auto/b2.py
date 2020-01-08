import os

print('启动项目！')

cmd = 'nohup python3 ../blog.py > ../out.log &'

print()
print('http://127.0.0.1:8081')

os.system(cmd)

