#Algoritmo genetico basico que resuelve problemas parametricos o combinatorios
#CarlosAEH1

def mutar(cromosomas, probabilidad):
	for i in range(len(cromosomas)):
		cromosoma=cromosomas[i]
		for j in range(len(cromosoma)):
			aleatorio=random.random()
			if(aleatorio<=probabilidad):
				if(cromosoma[j]==0): cromosoma[j]=1
				else: cromosoma[j]=0
		cromosomas[i]=cromosoma
	return cromosomas

def cruzar(cromosomas, probabilidad):
	indicesCruza=[]
	for i in range(len(cromosomas)):
		aleatorio=random.random()
		if(aleatorio<=probabilidad):							#Seleeciona cromosomas a cruzarse
			indicesCruza+=[i]
	if(len(indicesCruza)%2==1): del indicesCruza[-1]					#Verifica cantidad par de crozomas a cruzarse
	pareja=[]
	cromosomasCruzados=[]
	for i in range(len(cromosomas)):
		for j in range(len(indicesCruza)):
			if(i==indicesCruza[j]): pareja+=[cromosomas[i]]				#Busca cromosoma a cruzarse
		if(len(pareja)==2):								#Cruza cromosomas
			padre1=pareja[0]
			padre2=pareja[1]
			pareja=[]
			posicion=random.randrange(len(cromosomas[i]))
			hijo1=[]
			hijo2=[]
			for k in range(len(cromosomas[i])):
				if(k<posicion):
					hijo1+=[padre1[k]]
					hijo2+=[padre2[k]]
				else:
					hijo1+=[padre2[k]]
					hijo2+=[padre1[k]]
			cromosomasCruzados+=[hijo1]+[hijo2]
	for i in range(len(cromosomas)):							#Sustituye cromosomas originales
		for j in range(len(indicesCruza)):
			if(i==indicesCruza[j]): cromosomas[i]=cromosomasCruzados[j]
	return cromosomas

def seleccionar(cromosomas, aptitudesRelativas, opcionSeleccion):
	aptitudAcumulada=0
	aptitudesAcumuladas=[]
	for i in range(len(aptitudesRelativas)):							#Calcula aptitud acumulada
		aptitudAcumulada+=aptitudesRelativas[i]
		aptitudesAcumuladas+=[aptitudAcumulada]
	cromosomasSeleccionados=[]
	for i in range(len(cromosomas)):								#Selecciona cromosomas
		aleatorio=random.random()
		for j in range(len(aptitudesAcumuladas)):
			if(aptitudesAcumuladas[j]>aleatorio):
				if(opcionSeleccion==1): cromosomasSeleccionados+=[cromosomas[j]]	#Maximizacion de aptitud acumulada
				elif(opcionSeleccion==2): cromosomasSeleccionados+=[cromosomas[j-1]]	#Minimizacion de aptitud acumulada
				break
	return cromosomasSeleccionados

def mejorar(cromosomas, utilidades, opcionSeleccion, cromosomaElitista, utilidadElitistaAnterior):
	if(opcionSeleccion==1):										#Obtiene el mejor cromosoma
		utilidadElitistaActual=max(utilidades)
		if(utilidadElitistaAnterior is None): utilidadElitistaAnterior=utilidadElitistaActual
		if(utilidadElitistaAnterior>utilidadElitistaActual):					#Sustituye peor cromosoma por mejor cromosoma
			utilidadVulgar=min(utilidades)
			posicion=utilidades.index(utilidadVulgar)
			cromosomas[posicion]=cromosomaElitista
			utilidades[posicion]=utilidadElitistaAnterior
			utilidadElitistaActual=utilidadElitistaAnterior
		else:
			posicion=utilidades.index(utilidadElitistaActual)
			cromosomaElitista=cromosomas[posicion]
	elif(opcionSeleccion==2):									#Obtiene el mejor cromosoma
		utilidadElitistaActual=min(utilidades)
		if(utilidadElitistaAnterior is None): utilidadElitistaAnterior=utilidadElitistaActual
		if(utilidadElitistaAnterior<utilidadElitistaActual):					#Sustituye peor cromosoma por mejor cromosoma
			utilidadVulgar=max(utilidades)
			posicion=utilidades.index(utilidadVulgar)
			cromosomas[posicion]=cromosomaElitista
			utilidades[posicion]=utilidadElitistaAnterior
			utilidadElitistaActual=utilidadElitistaAnterior
		else:
			posicion=utilidades.index(utilidadElitistaActual)
			cromosomaElitista=cromosomas[posicion]
	return cromosomaElitista, utilidadElitistaActual

def codificarCromosoma(cromosoma, limite, numeros):
	bits=len(numeros[0])
	bit=0
	pesos=0
	numero=[]
	peso=[]
	while(bit<len(cromosoma)):			#Recorre cada bit
		numero+=[cromosoma[bit]]
		bit+=1
		if(len(numero)==bits):			#Divide cromosoma en grupos de 4 bits consecutivos
			pesos+=1
			for k in range(limite):		#Compara grupo de 4 bits con los numeros binarios
				if(numero==numeros[k]):
					peso+=[k]
					break
			if(pesos!=len(peso)): peso+=[0]	#Ignora numeros binarios no reconocidos
			numero=[]
	return peso

def codificarCromosomas(cromosomas, limite, numeros):
	pesos=[]
	for i in range(len(cromosomas)):
		cromosoma=cromosomas[i]
		peso=codificarCromosoma(cromosoma, limite,  numeros)
		pesos+=[peso]
	return pesos

def evaluarArbol(nodos, x, k):					#Recorre cromosoma como arbol en preorden
	if(nodos==[]):						#Agrega nodo varable o contante aleatoriamente
		nodos+=[random.choice((14, 15))]
		resultado=evaluarArbol(nodos, x, k)
	else:							#Opera nodo
		if(nodos[0]==0):
			del nodos[0]
			operando1=evaluarArbol(nodos, x, k)
			operando2=evaluarArbol(nodos, x, k)
			resultado=operando1+operando2
		elif(nodos[0]==1):
			del nodos[0]
			operando1=evaluarArbol(nodos, x, k)
			operando2=evaluarArbol(nodos, x, k)
			resultado=operando1-operando2
		elif(nodos[0]==2):
			del nodos[0]
			operando1=evaluarArbol(nodos, x, k)
			operando2=evaluarArbol(nodos, x, k)
			resultado=operando1*operando2
		elif(nodos[0]==3):
			del nodos[0]
			operando1=evaluarArbol(nodos, x, k)
			operando2=evaluarArbol(nodos, x, k)
			if(operando2==0): resultado=operando1
			else: resultado=operando1/operando2 
		elif(nodos[0]==4):
			del nodos[0]
			operando=evaluarArbol(nodos, x, k)
			if(operando<0): resultado=0
			else: resultado=math.sqrt(operando)
		elif(nodos[0]==5):
			del nodos[0]
			operando=evaluarArbol(nodos, x, k)
			if(operando<=0): resultado=0
			else: resultado=math.log(operando)
		elif(nodos[0]==6):
			del nodos[0]
			operando=evaluarArbol(nodos, x, k)
			resultado=math.sin(operando)
		elif(nodos[0]==7):
			del nodos[0]
			operando=evaluarArbol(nodos, x, k)
			resultado=math.cos(operando)
		elif(nodos[0]==8):
			del nodos[0]
			operando=evaluarArbol(nodos, x, k)
			resultado=math.tan(operando)
		elif(nodos[0]==9):
			del nodos[0]
			operando=evaluarArbol(nodos, x, k)
			resultado=abs(operando)
		elif(nodos[0]==10):
			del nodos[0]
			operando=evaluarArbol(nodos, x, k)
			resultado=-operando
		elif(nodos[0]==11):
			del nodos[0]
			operando=evaluarArbol(nodos, x, k)
			if(operando==0): resultado=0
			else: resultado=1/operando
		elif(nodos[0]==12):
			del nodos[0]
			operando1=evaluarArbol(nodos, x, k)
			operando2=evaluarArbol(nodos, x, k)
			resultado=max(operando1, operando2)
		elif(nodos[0]==13):
			del nodos[0]
			operando1=evaluarArbol(nodos, x, k)
			operando2=evaluarArbol(nodos, x, k)
			resultado=min(operando1, operando2)
		elif(nodos[0]==14):
			del nodos[0]
			resultado=x
		elif(nodos[0]==15):
			del nodos[0]
			resultado=k
	return resultado

def evaluarCombinatorioProgramacion(cromosomas, nombre, numeros, opcionSeleccion, cromosomaElitista, utilidadElitistaAnterior):
	contenido=open(nombre+'.txt')
	coordenadas=[]
	for linea in contenido: coordenadas+=[linea.rstrip().split('\t')]							#Obtiene coordendas de archivo TXT
	pesos=codificarCromosomas(cromosomas, len(numeros), numeros)
	resultados=[]
	errores=[]
	utilidades=[]
	for i in range(len(pesos)):
		pesosCromosoma=pesos[i]
		k=random.random()
		resultadosCromosoma=[]
		erroresCromosoma=[]
		for j in range(len(coordenadas)):
			coordenada=coordenadas[j]												#Selecciona coordenada
			nodos=pesosCromosoma[:]
			resultado=evaluarArbol(nodos, float(coordenada[0]), k)									#Evalua cromosoma
			resultadosCromosoma+=[resultado]
			erroresCromosoma+=[abs(float(coordenada[1])-resultado)]									#Calcula error absoluto
		resultados+=[resultadosCromosoma]
		errores+=[erroresCromosoma]
		if float('inf') in erroresCromosoma:
			posicion=erroresCromosoma.index(float('inf'))
			erroresCromosomaFinitos=erroresCromosoma[:]
			del erroresCromosomaFinitos[posicion]											#Calcula utilidad de cromosoma
		utilidades+=[sum(erroresCromosomaFinitos)]
	cromosomaElitista, utilidadElitistaActual=mejorar(cromosomas, utilidades, opcionSeleccion, cromosomaElitista, utilidadElitistaAnterior)	#Implementa elitismo
	aptitud=sum(utilidades)
	aptitudes=[]
	for i in range(len(utilidades)): aptitudes+=[utilidades[i]/aptitud]
	return aptitudes, cromosomaElitista, utilidadElitistaActual, aptitud

def evaluarCombinatorioViajero(cromosomas, nombre, hoja, puntos, numeros, opcionSeleccion, cromosomaElitista, utilidadElitistaAnterior):
	archivo=openpyxl.load_workbook(nombre+'.xlsx')
	pagina=archivo.get_sheet_by_name(hoja)
	distancias=[]
	for row in pagina.iter_rows():														#Obtiene matriz de distancias de archivo Excel
		punto=[]
		for i in range(puntos): punto+=[row[i].value]
		distancias+=[punto]
	pesos=codificarCromosomas(cromosomas, puntos, numeros)
	inutilidades=[]
	recorridos=[]
	utilidades=[]
	for i in range(len(pesos)):
		pesosCromosoma=pesos[i]
		inutilidad=1
		for j in range(len(pesosCromosoma)):												#Busca repeticiones
			valor=pesosCromosoma[j]
			j+=1
			while(j<len(pesosCromosoma)):
				if(valor==pesosCromosoma[j]): inutilidad+=1
				j+=1
		inutilidades+=[inutilidad]
		distancia=0
		for j in range(len(pesosCromosoma)):												#Calcula distancia de recorrido
			coordenada=pesosCromosoma[j]
			renglon=distancias[coordenada]
			if(j==0):														#Obtiene primer coordenada de recorrido
				coordenadaInicial=coordenada
				coordenadaSiguiente=pesosCromosoma[j+1]
				distancia+=renglon[coordenadaSiguiente]
			elif(j==len(pesosCromosoma)-1):	distancia+=renglon[coordenadaInicial]							#Cierra el recorrido con la coordenada inicial
			else:
				coordenadaSiguiente=pesosCromosoma[j+1]
				distancia+=renglon[coordenadaSiguiente]
		recorridos+=[distancia]
		if(opcionSeleccion==1): utilidades+=[distancia/inutilidad]									#Calcula utilidad de recorrido
		elif(opcionSeleccion==2): utilidades+=[distancia*inutilidad]
	cromosomaElitista, utilidadElitistaActual=mejorar(cromosomas, utilidades, opcionSeleccion, cromosomaElitista, utilidadElitistaAnterior)	#Implementa elitismo
	aptitud=sum(utilidades)															#Calcula aptitud total
	aptitudes=[]
	for i in range(len(utilidades)): aptitudes+=[utilidades[i]/aptitud]
	return aptitudes, cromosomaElitista, utilidadElitistaActual, aptitud

def evaluarCombinatorioReinas(cromosomas, reinas, numeros, opcionSeleccion, cromosomaElitista, utilidadElitistaAnterior):
	pesos=codificarCromosomas(cromosomas, reinas, numeros)
	utilidades=[]
	for i in range(len(pesos)):
		pesosCromosoma=pesos[i]
		utilidad=0
		for j in range(len(pesosCromosoma)):												#Busca repeticiones
			valor=pesosCromosoma[j]
			j+=1
			while(j<len(pesosCromosoma)):
				if(valor!=pesosCromosoma[j]): utilidad+=1
				j+=1
		for j in range(len(pesosCromosoma)):												#Busca secuencia hacia la derecha
			valor=pesosCromosoma[j]
			j+=1
			while(j<len(pesosCromosoma)):
				valor+=1
				if(valor==pesosCromosoma[j]): utilidad-=1
				j+=1
		for j in range(len(pesosCromosoma)-1, -1, -1):											#Busca secuencia hacia la izquierda
			valor=pesosCromosoma[j]
			j-=1
			while(j>=0):
				valor+=1
				if(valor==pesosCromosoma[j]): utilidad-=1
				j-=1
		utilidades+=[utilidad]
	cromosomaElitista, utilidadElitistaActual=mejorar(cromosomas, utilidades, opcionSeleccion, cromosomaElitista, utilidadElitistaAnterior)	#Implementa elitismo
	aptitud=sum(utilidades)															#Calcula aptitud total
	aptitudes=[]
	if(aptitud==0):
		for i in range(len(utilidades)): aptitudes+=[0]
	else:
		for i in range(len(utilidades)): aptitudes+=[utilidades[i]/aptitud]
	return aptitudes, cromosomaElitista, utilidadElitistaActual, aptitud

def evaluarParametrico(cromosomas, tamanoX, tamanoY, inferiorX, superiorX, inferiorY, superiorY, opcionFuncion, opcionSeleccion, cromosomaElitista, aptitudElitistaAnterior):
	funcion=0
	xDecimales=[]
	aptitudesFuncion=[]
	for i in range(len(cromosomas)):
		cromosoma=cromosomas[i]
		cromosomaX=[]
		cromosomaY=[]
		for j in range(len(cromosoma)):																				#Separa cromosoma en X y Y
			if(j<tamanoX): cromosomaX+=[cromosoma[j]]
			else: cromosomaY+=[cromosoma[j]]
		xBase2=[]
		for k in range(len(cromosomaX)-1, -1, -1): xBase2+=[cromosomaX[k]]															#Orden inverso de cromosoma
		xBase10=0
		for k in range(len(xBase2)): xBase10+=xBase2[k]*(2**k)																	#Convesion base 2 a base 10
		xDecimal=inferiorX+xBase10*((superiorX-inferiorX)/((2**tamanoX)-1))
		xDecimales+=[xDecimal]																					#Formato "flotante"
		yBase2=[]
		for k in range(len(cromosomaY)-1, -1, -1): yBase2+=[cromosomaY[k]]															#Orden inverso de cromosoma
		yBase10=0
		for k in range(len(yBase2)): yBase10+=yBase2[k]*(2**k)																	#Convesion base 2 a base 10
		yDecimal=inferiorY+yBase10*((superiorY-inferiorY)/((2**tamanoY)-1))															#Formato "flotante"
		if(opcionFuncion==1): funcion=-20*math.exp(-0.2*math.sqrt(0.5*((xDecimal**2)+(yDecimal**2))))-math.exp(0.5*(math.cos(2*math.pi*xDecimal)+math.cos(2*math.pi*yDecimal)))+math.e+20
		elif(opcionFuncion==2):
			if(i>=2):
				funcion+=100*((xDecimales[i]-xDecimales[i-1]**2)**2)+(1-xDecimales[i-1])**2
				aptitudesFuncion[i-1]=funcion
				if(i==len(cromosomas)-1): funcion+=100*((-xDecimales[i]**2)**2)+(1-xDecimales[i])**2
		elif(opcionFuncion==3): funcion=-(yDecimal+47)*math.sin(math.sqrt(abs((xDecimal/2)+yDecimal+47)))-xDecimal*math.sin(math.sqrt(abs(xDecimal-(yDecimal+47))))
		elif(opcionFuncion==4): funcion=((xDecimal**2+yDecimal-11)**2)+((xDecimal+yDecimal**2-7)**2)
		aptitudesFuncion+=[funcion]																				#Evalua funcion
	cromosomaElitista, aptitudElitistaActual=mejorar(cromosomas, aptitudesFuncion, opcionSeleccion, cromosomaElitista, aptitudElitistaAnterior)							#Imlementa elitismo
	aptitudPoblacion=sum(aptitudesFuncion)																				#Calcula aptitud total
	aptitudesRelativas=[]
	for i in range(len(aptitudesFuncion)): aptitudesRelativas+=[aptitudesFuncion[i]/aptitudPoblacion]												#Calcula aptitudes relativas
	return aptitudesRelativas, cromosomaElitista, aptitudElitistaActual, aptitudPoblacion

def generarPoblacion(tamanoCromosomas, tamanoPoblacion):
	cromosomas=[]
	if(tamanoPoblacion>1):
		for i in range(tamanoPoblacion):
			cromosoma=[]
			for j in range(tamanoCromosoma): cromosoma+=[random.choice((0, 1))]
			cromosomas+=[cromosoma]
		return cromosomas
	else: print('\nError, introduciste un tamaño de población de cromosomas menor o igual a 1.')

numeros=[[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]] #Numeros binarios

cromosomas=generarPoblacion(tamanoCromosoma, tamanoPoblacion)
aptitudesRelativas, cromosomaElitista, aptitudElitista, aptitudPoblacion=evaluarParametrico(cromosomas, tamanoX, tamanoY, inferiorX, superiorX, inferiorY, superiorY, opcionFuncion, opcionSeleccion, None, None)
aptitudesElitistasEjecucion+=[aptitudElitista]
aptitudesPoblacionEjecucion+=[aptitudPoblacion]
for j in range(generaciones):
	cromosomas=seleccionar(cromosomas, aptitudesRelativas, opcionSeleccion)
	cromosomas=cruzar(cromosomas, probabilidadCruza)
	cromosomas=mutar(cromosomas, probabilidadMutacion)
	aptitudesRelativas, cromosomaElitista, aptitudElitista, aptitudPoblacion=evaluarParametrico(cromosomas, tamanoX, tamanoY, inferiorX, superiorX, inferiorY, superiorY, opcionFuncion, opcionSeleccion, cromosomaElitista, aptitudElitista)