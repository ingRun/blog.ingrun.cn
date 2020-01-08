import subprocess

ls: list = []
cmd = 'ps -ef | grep blog.py'

p = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)

out = str(p.stdout, 'utf-8').split('\n')

for i in range(len(out)-1):
    link = out[i].split(' ')
    ls = []
    for k in (link):
        if k is not ' ' and k is not '':
            ls.append(k)

    cmd = f'kill -9 {ls[1]}'
    subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
