import subprocess
    
cpu_temp = subprocess.run(["sensors"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True).stdout.split('\n')

for line in cpu_temp:
    if "Tctl:" in line:
        print(line.split('+')[1])

