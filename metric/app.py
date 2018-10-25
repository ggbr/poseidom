import psutil
import time
import pymongo
import urllib.request

host = "192.168.1.24"


myclient = pymongo.MongoClient('mongodb://mongodb:27017/')
mydb = myclient['metric']
mycol = mydb["host"]



def status():
    cpu = str(psutil.cpu_percent(interval=1))
    m =  psutil.virtual_memory()
    memoria =  str(m.percent)
    
    diskDir = psutil.disk_usage('/')
    disk = str(diskDir.percent)
    list  = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=[ 'name'])
        except psutil.NoSuchProcess:
            pass
        else:
            if not pinfo['name'] in list:
                list.append(pinfo['name'])
    print("CPU - "+ cpu)            
    print("Mem - " + memoria)            
    print("Disk - " + disk)            
    print("Pross -" + str(list) )            
    save(cpu,memoria,disk,list)
    alert(cpu)
    
def save(cpu,memorria,disk,process):
    mydict = { "cpu": cpu , "memoria": memorria, "disk" :disk, "process":process}

    x = mycol.insert_one(mydict)


def alert(cpu):
    if float(cpu) > 70:

        source = 'http://' +host +':3000'

        with urllib.request.urlopen(source+ '/a') as response:
            html = response.read()

        print("Enviando alerta...")

while True:
    status()

    time.sleep(2)