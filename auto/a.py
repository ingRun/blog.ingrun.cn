import os

print('同步远程仓库开始！')

cmd = 'git fetch --all && git reset --hard origin/master && git pull && echo 同步远程仓库完成'
os.system(cmd)

