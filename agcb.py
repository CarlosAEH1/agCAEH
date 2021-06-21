#Algoritmo genetico basico que resuelve problemas parametricos o combinatorios
#CarlosAEH1

def mostrarCromosomas(cromosomas):
	print('\n\nPoblacion\n')
	for i in range(len(cromosomas)): print('Cromosoma ', i+1, ': '+str(cromosomas[i]))

def mutar(cromosomas, probabilidad):
	#print('\n\nMutacion')
	for i in range(len(cromosomas)):
		#print('\nCromosoma ', i+1)
		cromosoma=cromosomas[i]
		for j in range(len(cromosoma)):
			aleatorio=random.random()
			if(aleatorio<=probabilidad):
				#print('-Posicion ', j, ', con numero aleatorio: ', aleatorio)
				if(cromosoma[j]==0): cromosoma[j]=1
				else: cromosoma[j]=0
		cromosomas[i]=cromosoma
	#mostrarCromosomas(cromosomas)
	return cromosomas

def cruzar(cromosomas, probabilidad):
	#print('\n\nCruza\n')
	indicesCruza=[]
	for i in range(len(cromosomas)):
		aleatorio=random.random()
		if(aleatorio<=probabilidad):							#Seleeciona cromosomas a cruzarse
			#print('Cromosoma ', i+1, ', con numero aleatorio: ', aleatorio)
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
			#print('\nPadre 1: ', padre1)
			#print('Padre 2: ', padre2)
			posicion=random.randrange(len(cromosomas[i]))
			#print('\nPosicion de cruza: ', posicion)
			hijo1=[]
			hijo2=[]
			for k in range(len(cromosomas[i])):
				if(k<posicion):
					hijo1+=[padre1[k]]
					hijo2+=[padre2[k]]
				else:
					hijo1+=[padre2[k]]
					hijo2+=[padre1[k]]
			#print('\nHijo 1: ', hijo1)
			#print('Hijo 2: ', hijo2)
			cromosomasCruzados+=[hijo1]+[hijo2]
	for i in range(len(cromosomas)):							#Sustituye cromosomas originales
		for j in range(len(indicesCruza)):
			if(i==indicesCruza[j]): cromosomas[i]=cromosomasCruzados[j]
	#mostrarCromosomas(cromosomas)
	return cromosomas

def seleccionar(cromosomas, aptitudesRelativas, opcionSeleccion):
	#print('\n\nSelecion\n')
	aptitudAcumulada=0
	aptitudesAcumuladas=[]
	#print('Cromosoma\tAptitud relativa\tAptitud acumulada')
	for i in range(len(aptitudesRelativas)):							#Calcula aptitud acumulada
		aptitudAcumulada+=aptitudesRelativas[i]
		#print(str(i+1)+'\t'+str(aptitudesRelativas[i])+'\t'+str(aptitudAcumulada))
		aptitudesAcumuladas+=[aptitudAcumulada]
	cromosomasSeleccionados=[]
	#print('\n')
	for i in range(len(cromosomas)):								#Selecciona cromosomas
		aleatorio=random.random()
		for j in range(len(aptitudesAcumuladas)):
			if(aptitudesAcumuladas[j]>aleatorio):
				if(opcionSeleccion==1): cromosomasSeleccionados+=[cromosomas[j]]	#Maximizacion de aptitud acumulada
				elif(opcionSeleccion==2): cromosomasSeleccionados+=[cromosomas[j-1]]	#Minimizacion de aptitud acumulada
				break
	#mostrarCromosomas(cromosomasSeleccionados)
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

def codificarCromosomaCombinatorio(cromosoma, limite, numeros):
	bits=len(numeros[0])
	bit=0
	pesos=0
	numero=[]
	peso=[]
	while(bit<len(cromosoma)):				#Recorre cada bit
		numero+=[cromosoma[bit]]
		bit+=1
		if(len(numero)==bits):				#Divide cromosoma en grupos de 4 bits consecutivos
			pesos+=1
			for k in range(limite):			#Compara grupo de 4 bits con los numeros binarios
				if(numero==numeros[k]):
					peso+=[k]
					break
			if(pesos!=len(peso)): peso+=[0]		#Ignora numeros binarios no reconocidos
			numero=[]
	#print('-Peso: '+str(peso))
	return peso

def codificarCromosomasCombinatorio(cromosomas, limite, numeros):
	pesos=[]
	for i in range(len(cromosomas)):
		cromosoma=cromosomas[i]
		peso=codificarCromosomaCombinatorio(cromosoma, limite,  numeros)
		pesos+=[peso]
	#print('\nPesos de cromosomas: ')
	#for i in range(len(pesos)): print('-Cromosoma ', i+1, ': ', pesos[i])
	return pesos

def codificarCromosomaParametrico(cromosoma, tamanoX, tamanoY, inferiorX, superiorX, inferiorY, superiorY, xDecimales):
	cromosomaX=[]
	cromosomaY=[]
	for j in range(len(cromosoma)):											#Separa cromosoma en X y Y
		if(j<tamanoX): cromosomaX+=[cromosoma[j]]
		else: cromosomaY+=[cromosoma[j]]
	#print('X en base 2: ', cromosomaX)
	xBase2=[]
	for k in range(len(cromosomaX)-1, -1, -1): xBase2+=[cromosomaX[k]]						#Orden inverso de cromosoma
	xBase10=0
	for k in range(len(xBase2)): xBase10+=xBase2[k]*(2**k)								#Convesion base 2 a base 10
	#print('X en base 10: ', xBase10)
	xDecimal=inferiorX+xBase10*((superiorX-inferiorX)/((2**tamanoX)-1))
	if(xDecimales!=None): xDecimales+=[xDecimal]																					#Formato "flotante"
	#print('X en decimal: ', xDecimal)
	#print('Y en base 2: ', cromosomaY)
	yBase2=[]
	for k in range(len(cromosomaY)-1, -1, -1): yBase2+=[cromosomaY[k]]						#Orden inverso de cromosoma
	yBase10=0
	for k in range(len(yBase2)): yBase10+=yBase2[k]*(2**k)								#Convesion base 2 a base 10
	#print('Y en base 10: ', yBase10)
	yDecimal=inferiorY+yBase10*((superiorY-inferiorY)/((2**tamanoY)-1))						#Formato "flotante"
	#print('Y en decimal: ', yDecimal)
	return xDecimal, xDecimales, yDecimal

def evaluarArbolBooleano(nodos, entrada, nivel, profundidad):					#Recorre cromosoma como arbol en preorden
	#print('Nodos: ', nodos)
	#print('Nivel: ', nivel)
	#print('Profundidad: ', profundidad)
	if(nivel<profundidad):									#Opera nodo
		if(nodos[0]==0):
			del nodos[0]
			operando1=evaluarArbolBooleano(nodos, entrada, nivel+1, profundidad)
			operando2=evaluarArbolBooleano(nodos, entrada, nivel+1, profundidad)
			salida=(operando1 and operando2)
			nivel-=1
		elif(nodos[0]==1):
			del nodos[0]
			operando1=evaluarArbolBooleano(nodos, entrada, nivel+1, profundidad)
			operando2=evaluarArbolBooleano(nodos, entrada, nivel+1, profundidad)
			salida=(operando1 or operando2)
			nivel-=1
		elif(nodos[0]==2):
			del nodos[0]
			operando=evaluarArbolBooleano(nodos, entrada, nivel+1, profundidad)
			salida=not(operando)
			nivel-=1
		elif(nodos[0]==3):
			del nodos[0]
			operando1=evaluarArbolBooleano(nodos, entrada, nivel+1, profundidad)
			operando2=evaluarArbolBooleano(nodos, entrada, nivel+1, profundidad)
			salida=(operador1 and not(operador2))or(not(operador1) and operador2)
			nivel-=1
	else:
		del nodos[0]									#Agrega nodo varable o contante aleatoriamente
		salida=bool(entrada[0])
		#print('Entrada: ', salida)
		del entrada[0]
	return salida

def evaluarArbolAlgebraico(nodos, entrada, nivel, profundidad):					#Recorre cromosoma como arbol en preorden
	#print('Nodos: ', nodos)
	#print('Nivel: ', nivel)
	#print('Profundidad: ', profundidad)
	if(nivel<profundidad):									#Opera nodo
		if(nodos[0]==0):
			del nodos[0]
			operando1=evaluarArbolAlgebraico(nodos, entrada, nivel+1, profundidad)
			operando2=evaluarArbolAlgebraico(nodos, entrada, nivel+1, profundidad)
			resultado=operando1+operando2
			nivel-=1
		elif(nodos[0]==1):
			del nodos[0]
			operando1=evaluarArbolAlgebraico(nodos, entrada, nivel+1, profundidad)
			operando2=evaluarArbolAlgebraico(nodos, entrada, nivel+1, profundidad)
			resultado=operando1-operando2
			nivel-=1
		elif(nodos[0]==2):
			del nodos[0]
			operando1=evaluarArbolAlgebraico(nodos, entrada, nivel+1, profundidad)
			operando2=evaluarArbolAlgebraico(nodos, entrada, nivel+1, profundidad)
			resultado=operando1*operando2
			nivel-=1
		elif(nodos[0]==3):
			del nodos[0]
			operando1=evaluarArbolAlgebraico(nodos, entrada, nivel+1, profundidad)
			operando2=evaluarArbolAlgebraico(nodos, entrada, nivel+1, profundidad)
			if(operando2==0): resultado=operando1
			else: resultado=operando1/operando2
			nivel-=1
		elif(nodos[0]==4):
			del nodos[0]
			operando=evaluarArbolAlgebraico(nodos, entrada, nivel+1, profundidad)
			resultado=math.sin(operando)
			nivel-=1
		elif(nodos[0]==5):
			del nodos[0]
			operando=evaluarArbolAlgebraico(nodos, entrada, nivel+1, profundidad)
			resultado=math.cos(operando)
			nivel-=1
		elif(nodos[0]==6):
			del nodos[0]
			operando=evaluarArbolAlgebraico(nodos, entrada, nivel+1, profundidad)
			resultado=math.tan(operando)
			nivel-=1
		elif(nodos[0]==7):
			del nodos[0]
			operando1=evaluarArbolAlgebraico(nodos, entrada, nivel+1, profundidad)
			operando2=evaluarArbolAlgebraico(nodos, entrada, nivel+1, profundidad)
			resultado=operando1**operando2
			nivel-=1
		elif(nodos[0]==8):
			del nodos[0]
			operando=evaluarArbolAlgebraico(nodos, entrada, nivel+1, profundidad)
			if(operando<0): resultado=0
			else: resultado=math.sqrt(operando)
			nivel-=1
		elif(nodos[0]==9):
			del nodos[0]
			operando=evaluarArbolAlgebraico(nodos, entrada, nivel+1, profundidad)
			resultado=math.exp(operando)
			nivel-=1
		elif(nodos[0]==10):
			del nodos[0]
			operando=evaluarArbolAlgebraico(nodos, entrada, nivel+1, profundidad)
			if(operando<=0): resultado=0
			else: resultado=math.log(operando)
			nivel-=1
	else:
		del nodos[0]									#Agrega nodo varable o contante aleatoriamente
		resultado=entrada[0]
		#print('Entrada: ', resultado)
		del entrada[0]
	return resultado

def evaluarCombinatorioProgramacion(cromosomas, inferiorX, superiorX, profundidad, nombre, numeros, opcionProblema, opcionSeleccion, cromosomaElitista, utilidadElitistaAnterior):
	resultadoFuncion=[1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1]
	#print('\n\nEvaluación')
	"""contenido=open(nombre+'.txt')
	coordenadas=[]
	for linea in contenido: coordenadas+=[linea.rstrip().split('\t')]														#Obtiene coordendas de archivo TXT
	print('\nCoordenadas')
	for i in range(len(coordenadas)): print(coordenadas[i])"""
	if(opcionProblema==1): pesos=codificarCromosomasCombinatorio(cromosomas, 10, numeros)
	elif(opcionProblema==2): pesos=codificarCromosomasCombinatorio(cromosomas, 3, numeros)
	resultados=[]
	errores=[]
	utilidades=[]
	for i in range(len(pesos)):
		pesosCromosoma=pesos[i]
		resultadosCromosoma=[]
		erroresCromosoma=[]
		if(opcionProblema==1):
			k=random.random()
			#print('\nAleatorio de cromosoma ', i+1, ': ', k)
			operandos=[]
			for j in range(2**profundidad): operandos+=[random.choice((0, 1))]												#Prepara lista de terminales
			x=inferiorX
			while(x<=superiorX):																		#Recorre rango de variable independiente
				resultadoFuncion=((-2.34**3)-(-0.11*x/2))+23.45														#Evalua funcion
				#print('\n-Resultado de funcion: '+str(resultadoFuncion))
				nodos=pesosCromosoma[:]
				for j in range(2**profundidad):																#Genera lista de terminales a evaluar
					if(operandos[j]==0): operandos[j]=x
					else: operandos[j]=k
				entrada=operandos[:]
				resultadoCromosoma=evaluarArbolAlgebraico(nodos, entrada, 0, profundidad)										#Evalua cromosoma
				#print('-Resultado de cromosoma: '+str(resultadoCromosoma))
				resultadosCromosoma+=[resultadoCromosoma]
				erroresCromosoma+=[abs(resultadoFuncion-resultadoCromosoma)]												#Calcula error absoluto
				#print('Errores de cromosoma: '+str(erroresCromosoma))
				x=round(x+0.1, 1)
		elif(opcionProblema==2):
			for j in range(len(numeros)):
				nodos=pesosCromosoma[:]
				numero=numeros[j]
				entrada=numero[:]
				salida=evaluarArbolBooleano(nodos, entrada, 0, profundidad)												#Evalua cromosoma
				#print('Resultado de cromosoma: '+str(salida))
				resultadosCromosoma+=[int(salida)]
				erroresCromosoma+=[abs(resultadoFuncion[j]-int(salida))]												#Calcula error absoluto
				#print('Errores de cromosoma: '+str(erroresCromosoma))
		else:
			"""k=random.random()
			#print('-Aleatorio de cromosoma ', i+1, ': ', str(k))
			for j in range(len(coordenadas)):
				coordenada=coordenadas[j]																#Selecciona coordenada
				nodos=pesosCromosoma[:]
				resultado=evaluarArbol(nodos, float(coordenada[0]), k)													#Evalua cromosoma
				resultadosCromosoma+=[resultado]
				erroresCromosoma+=[abs(float(coordenada[1])-resultado)]"""												#Calcula error absoluto
		resultados+=[resultadosCromosoma]
		errores+=[erroresCromosoma]
		if float('inf') in erroresCromosoma:
			posicion=erroresCromosoma.index(float('inf'))
			del erroresCromosoma[posicion]																	#Calcula utilidad de cromosoma
		utilidades+=[sum(erroresCromosoma)]
	#print('\nResultados de cromosomas: ')
	#for i in range(len(resultados)): print('-Cromosoma ', i+1, ': ', resultados[i])
	#print('\nErrores de cromosomas: ')
	#for i in range(len(errores)): print('-Cromosoma ', i+1, ': ', errores[i])
	#print('\nError de cromosomas: ')
	#for i in range(len(utilidades)): print('-Cromosoma ', i+1, ': ', utilidades[i])
	cromosomaElitista, utilidadElitistaActual=mejorar(cromosomas, utilidades, opcionSeleccion, cromosomaElitista, utilidadElitistaAnterior)	#Implementa elitismo
	aptitud=sum(utilidades)
	#print('\nUtilidad de la poblacion: ', aptitud)
	aptitudes=[]
	for i in range(len(utilidades)): aptitudes+=[utilidades[i]/aptitud]
	return aptitudes, cromosomaElitista, utilidadElitistaActual, aptitud

def evaluarCombinatorioViajero(cromosomas, nombre, hoja, puntos, numeros, opcionSeleccion, cromosomaElitista, utilidadElitistaAnterior):
	#print('\n\nEvaluación')
	archivo=openpyxl.load_workbook(nombre+'.xlsx')
	pagina=archivo.get_sheet_by_name(hoja)
	distancias=[]
	for row in pagina.iter_rows():														#Obtiene matriz de distancias de archivo Excel
		punto=[]
		for i in range(puntos): punto+=[row[i].value]
		distancias+=[punto]
	#print('Matriz de distancias')
	#for i in range(puntos): print(distancias[i])
	pesos=codificarCromosomasCombinatorio(cromosomas, puntos, numeros)
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
	#print('\nInutilidad de cromosomas: ')
	#for i in range(len(inutilidades)): print('-Cromosoma ', i+1, ': ', inutilidades[i])
	#print('\nDistancia recorrida de cromosomas: ')
	#for i in range(len(recorridos)): print('-Cromosoma ', i+1, ': ', recorridos[i])		
	#print('\nUtilidad de cromosomas: ')
	#for i in range(len(utilidades)): print('-Cromosoma ', i+1, ': ', utilidades[i])
	cromosomaElitista, utilidadElitistaActual=mejorar(cromosomas, utilidades, opcionSeleccion, cromosomaElitista, utilidadElitistaAnterior)	#Implementa elitismo
	aptitud=sum(utilidades)															#Calcula aptitud total
	#print('\nUtilidad de la poblacion: ', aptitud)
	aptitudes=[]
	for i in range(len(utilidades)): aptitudes+=[utilidades[i]/aptitud]
	return aptitudes, cromosomaElitista, utilidadElitistaActual, aptitud

def evaluarCombinatorioReinas(cromosomas, reinas, numeros, opcionSeleccion, cromosomaElitista, utilidadElitistaAnterior):
	#print('\n\nEvaluación')
	pesos=codificarCromosomasCombinatorio(cromosomas, reinas, numeros)
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
	#print('\nUtilidad de cromosomas: ')
	#for i in range(len(utilidades)): print('-Cromosoma ', i+1, ': ', utilidades[i])
	cromosomaElitista, utilidadElitistaActual=mejorar(cromosomas, utilidades, opcionSeleccion, cromosomaElitista, utilidadElitistaAnterior)	#Implementa elitismo
	aptitud=sum(utilidades)															#Calcula aptitud total
	#print('\nUtilidad de la poblacion: ', aptitud)
	aptitudes=[]
	if(aptitud==0):
		for i in range(len(utilidades)): aptitudes+=[0]
	else:
		for i in range(len(utilidades)): aptitudes+=[utilidades[i]/aptitud]
	return aptitudes, cromosomaElitista, utilidadElitistaActual, aptitud

def evaluarParametrico(cromosomas, tamanoX, tamanoY, inferiorX, superiorX, inferiorY, superiorY, opcionFuncion, opcionSeleccion, cromosomaElitista, aptitudElitistaAnterior):
	#print('\n\nEvaluación')
	funcion=0
	xDecimales=[]
	aptitudesFuncion=[]
	for i in range(len(cromosomas)):
		#print('\nCromosoma', i+1)
		cromosoma=cromosomas[i]
		xDecimal, xDecimales, yDecimal=codificarCromosomaParametrico(cromosoma, tamanoX, tamanoY, inferiorX, superiorX, inferiorY, superiorY, xDecimales)
		if(opcionFuncion==1): funcion=-20*math.exp(-0.2*math.sqrt(0.5*((xDecimal**2)+(yDecimal**2))))-math.exp(0.5*(math.cos(2*math.pi*xDecimal)+math.cos(2*math.pi*yDecimal)))+math.e+20
		elif(opcionFuncion==2):
			if(i>=2):
				funcion+=100*((xDecimales[i]-xDecimales[i-1]**2)**2)+(1-xDecimales[i-1])**2
				aptitudesFuncion[i-1]=funcion
				if(i==len(cromosomas)-1): funcion+=100*((-xDecimales[i]**2)**2)+(1-xDecimales[i])**2
		elif(opcionFuncion==3): funcion=-(yDecimal+47)*math.sin(math.sqrt(abs((xDecimal/2)+yDecimal+47)))-xDecimal*math.sin(math.sqrt(abs(xDecimal-(yDecimal+47))))
		elif(opcionFuncion==4): funcion=((xDecimal**2+yDecimal-11)**2)+((xDecimal+yDecimal**2-7)**2)
		aptitudesFuncion+=[funcion]																				#Evalua funcion
	#print('\nResultados')
	#for i in range(len(aptitudesFuncion)): print('-Cromosoma ', i+1, ': '+str(aptitudesFuncion[i]))
	cromosomaElitista, aptitudElitistaActual=mejorar(cromosomas, aptitudesFuncion, opcionSeleccion, cromosomaElitista, aptitudElitistaAnterior)							#Imlementa elitismo
	aptitudPoblacion=sum(aptitudesFuncion)																				#Calcula aptitud total
	#print('\nAptitud de la poblacion: ', aptitudPoblacion)
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
		#mostrarCromosomas(cromosomas)
		return cromosomas
	else: print('\nError, introduciste un tamaño de población de cromosomas menor o igual a 1.')

numeros=[[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]] #Numeros binarios

cromosomas=generarPoblacion(tamanoCromosoma, tamanoPoblacion)
aptitudesRelativas, cromosomaElitista, aptitudElitista, aptitudPoblacion=evaluarParametrico(cromosomas, tamanoX, tamanoY, inferiorX, superiorX, inferiorY, superiorY, opcionFuncion, opcionSeleccion, None, None)
#aptitudes, cromosomaElitista, utilidadElitista, aptitud=evaluarCombinatorioReinas(cromosomas, reinas, numeros, opcionSeleccion, None, None)
#aptitudes, cromosomaElitista, utilidadElitista, aptitud=evaluarCombinatorioViajero(cromosomas, nombre, hoja, puntos, numeros, opcionSeleccion, None, None)
#aptitudes, cromosomaElitista, utilidadElitista, aptitud=evaluarCombinatorioProgramacion(cromosomas, nombre, numeros, opcionSeleccion, None, None)
for j in range(generaciones):
	cromosomas=seleccionar(cromosomas, aptitudesRelativas, opcionSeleccion)
	cromosomas=cruzar(cromosomas, probabilidadCruza)
	cromosomas=mutar(cromosomas, probabilidadMutacion)
	aptitudesRelativas, cromosomaElitista, aptitudElitista, aptitudPoblacion=evaluarParametrico(cromosomas, tamanoX, tamanoY, inferiorX, superiorX, inferiorY, superiorY, opcionFuncion, opcionSeleccion, cromosomaElitista, aptitudElitista)
	#aptitudes, cromosomaElitista, utilidadElitista, aptitud=evaluarCombinatorioReinas(cromosomas, reinas, numeros, opcionSeleccion, cromosomaElitista, utilidadElitista)
	#aptitudes, cromosomaElitista, utilidadElitista, aptitud=evaluarCombinatorioViajero(cromosomas, nombre, hoja, puntos, numeros, opcionSeleccion, cromosomaElitista, utilidadElitista)
	#aptitudes, cromosomaElitista, utilidadElitista, aptitud=evaluarCombinatorioProgramacion(cromosomas, nombre, numeros, opcionSeleccion, cromosomaElitista, utilidadElitista)