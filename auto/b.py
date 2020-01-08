import subprocess

cmd = 'nohup ../venv/bin/python3 ../blog.py > ../out.log &'

subprocess.run(cmd, shell=True)

print()
print('http://127.0.0.1:8081')
print('http://192.168.43.70:8081')
print()
