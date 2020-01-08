import subprocess

cmd = 'nohup ../venv/bin/python3 ../blog.py > ../out.log &'

subprocess.run(cmd, shell=True)

print()
print('http://127.0.0.1')
print()