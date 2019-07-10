import time
import random
fila = []
#cada pacote vai ter um tamanho que varia de 1 a 5
#com valores aleatórios de 0 a 100.

#Considerando a primeira posição da lista do pacote como sendo
#o cabeçalho, se o valor for maior que 50, ele será direcionado
#para o roteador A, do contrário para o roteador B.

taxaTrans = 1 #taxa de transmissão: 1 posição do vetor por segundo
velPropag = 1 #velocidade de propagação
distancia = 3 #distancia para um roteador qualquer
def atrasoPropagacao(pacote):
	atraso = distancia/velPropag
	print("Levando pacote para o proximo roteador...")
	time.sleep(atraso)
	print("Tempo de espera: ", atraso)
	return atraso
def atrasoTransmissao(pacote):
	atraso = len(pacote)/taxaTrans
	print("Transmitindo pacote para o enlace...")
	time.sleep(atraso)
	print("Tempo de espera: ", atraso)
	return atraso
def atrasoFila(pacote):
	#aqui, para fins da simulação, assume-se que apenas um pacote
	#pode estar no enlace por vez.
	pacote.append(fila)
	acum = 0
	for pkg in fila:
		acum += atrasoTransmissao(pkg)
		acum += atrasoPropagacao(pkg)
	return acum
def atrasoProcessamento(pacote):
	#uma abstração de processamento do cabeçalho para definir para qual roteador será enviado
	if pacote[0] > 50:
		print("Processando...")
		time.sleep(1)
		print("Tempo de espera: 1")
		destino = "routerA"
		print(destino)
	else:
		print("Processando...")
		time.sleep(1)
		print("Tempo de espera: 1")
		destino = "routerB"
		print(destino)
	return 1+atrasoFila(pacote)

def enviaPacote():
	tam = random.randint(1, 5)
	pacote = [random.randint(0,100) for i in range(tam)]#cria o pacote em questão
	print("Este é o pacote a ser transmitido: ", pacote)
	print("----------Inicio da operação----------")
	atrasoNodalTotal = atrasoProcessamento(pacote)
	return atrasoNodalTotal
def populaFila(): #para simular o atraso de fila, são gerados pacotes para a fila.
	for i in range(random.randint(0, 3)):
		tam = random.randint(1, 3)
		pacote = [random.randint(0,100) for i in range(tam)]
		fila.append(pacote)

populaFila()
print("Fila no roteador:")
for pkg in fila:
	print(pkg)

atraso = enviaPacote()
print("Pacote enviado!")
print("Atraso de envio, em segundos:", atraso)		