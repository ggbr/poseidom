import psutil
from pymongo import MongoClient

print(psutil.cpu_percent(interval=1))
memoria =  psutil.virtual_memory()
print(memoria.percent)
disk = psutil.disk_usage('/')

print(disk.percent)
list  = []
for proc in psutil.process_iter():
    try:
        pinfo = proc.as_dict(attrs=[ 'name'])
    except psutil.NoSuchProcess:
        pass
    else:
        

        if not pinfo['name'] in list:

            list.append(pinfo['name'])

print(list)