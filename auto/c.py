import subprocess

cmd = 'ps -ef | grep blog.py'

p = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)

out = str(p.stdout, 'utf-8').split('\n')

for i in range(len(out)-1):
    link = out[i].split('     ')
    link = link[1]
    link = link.split('  ')
    print(link[0])

    cmd = f'kill -9 {link[0]}'
    subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)