import os

for ip in range(7):
    os.system('ping -c 1 192.168.0.' + str(ip))
print('Done')
