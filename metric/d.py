import docker
client = docker.from_env()
conteinerParado = 0
conteinerExecucao = 0

def stack(list):
    lista_stack_nomes = []
    for l in list:
        stack = l[0: l.find("_") ]
        if not stack in lista_stack_nomes:
            lista_stack_nomes.append(stack)
    return lista_stack_nomes


lintaConteines = []
for container in client.containers.list(all=True):
    lintaConteines.append(container.name)
    #print(container.name +" :"+container.status)
    if container.status == "exited":
        conteinerParado = conteinerParado + 1
    elif(container.status == "running"):
        conteinerExecucao = conteinerExecucao + 1

#print("Conteiner parados:" + str(conteinerParado))
#print("Conteiner enm Execução:" + str(conteinerExecucao))
#print(stack(lintaConteines))



##################################################
