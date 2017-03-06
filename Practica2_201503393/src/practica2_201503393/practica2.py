#from flask import Flask, request, Response
#app = Flask("Practica2")

class NodoMatriz:
	#derecha = NodoMatriz("")
	#izquierda = NodoMatriz("")
	#abajo = NodoMatriz("")
	#arriba = NodoMatriz("")
	#info = ""
	print "Funciona"

	def __init__(self, info):
		self.info = info
		#abajo = NodoMatriz("")
		#self.arriba = NodoMatriz("")
		#self.izquierda = NodoMatriz("")
		#self.derecha = NodoMatriz("")
		self.abajo= None
		self.arriba = None
		self.izquierda = None
		self.derecha = None

	def insertarCol(nuevo):
		if self.derecha != None:
			self.derecha.insertarCol(nuevo)
		else:
			self.derecha = nuevo
			this.derecha.izquierda=this.derecha

	def insertarFila(nuevo):
		if self.abajo != None:
			self.abajo.insertarFila(nuevo)
		else:
			this.abajo = nuevo
			this.abajo.arriba = this.abajo

	def setInfo(info):
		self.info = info

	def getInfo():
		return self.info

class Matriz:
	#dispatch_dict = {"Foo": Foo, "Bar": Bar}
	#dispatch_dict["Foo"]() # returns an instance of Foo
	#self.cabeza = NodoMatriz("0")

	def __init__(self):
		self.cabeza = NodoMatriz("0")

	def nuevaCol(self, nuevo, aux):
		if aux == None:
			aux=self.cabeza
		if self.cabeza.derecha == None:
			self.cabeza.derecha=nuevo
			nuevo.izquierda =self.cabeza
			print "se creo el dom %s" %nuevo.info 
		else:
			aux = aux.derecha
			letra = aux.info[:1]
			nletra = nuevo.info[:1]
			if (ord(nletra) > ord(letra)):
				if aux.derecha != None:
					self.nuevaCol(nuevo, aux)  
				else:
					aux.derecha = nuevo
					nuevo.izquierda = aux
					print "se creo el dom %s" %nuevo.info 

			else:
				nuevo.derecha = aux.derecha
				#aux.derecha.izquierda = nuevo
				aux.derecha = nuevo
				#nuevo.izquierda = aux
				print "se creo el dom %s" %nuevo.info 

	def nuevaFila(self, nuevo, aux):
		if aux == None:
			aux=self.cabeza
		if self.cabeza.abajo == None:
			self.cabeza.abajo=nuevo
			nuevo.arriba=self.cabeza
			print "se creo la letra %s" %nuevo.info 
		else:
			aux = aux.abajo
			letra = aux.info
			nletra = nuevo.info
			if (ord(nletra) > ord(letra)):
				if aux.abajo != None:
					self.nuevaFila(nuevo, aux)
				else:
					aux.abajo = nuevo
					nuevo.arriba = aux
					print "se creo la letra %s" %nuevo.info 

			else:
				nuevo.abajo = aux.abajo
				#aux.abajo.arriba = nuevo
				aux.abajo = nuevo
				#nuevo.arriba = aux
				print "se creo la letra %s" %nuevo.info 

	#contadorf = 0
	#contadorc= 0
	def insertar(self, nfila, ncol, nuevo):
		aux1 = self.cabeza
		aux2 = self.cabeza
		b1 = False
		b2 = False
		while b1 == False:
			while aux1.derecha != None:
				aux1 = aux1.derecha
				if (aux1.info == ncol):
					b1 = True
					print "encontro el dom %s" %aux1.info 
					break	
			if b1==False:
				asd = NodoMatriz(ncol)
				nuevaCol(asd, self.cabeza)
				b1 = True
				insertar(nfila, ncol, nuevo, ninfo)

		while b2 == False:
			while aux2.abajo != None:
				aux2 = aux2.abajo
				if (aux2.info == nfila):
					b2 = True
					print "encontro la letra %s" %aux2.info 
					break
			if b2==False:
				asd = NodoMatriz(nfila)
				nuevaFila(asd, self.cabeza)
				b2 = True
				insertar(nfila, ncol, nuevo, ninfo)

		if aux1.abajo != None:
			nuevo = self.insertarC(nuevo,aux1)
		else:
			aux1.abajo = nuevo
			nuevo.arriba = aux1
			print "se creo la info %s" %nuevo.info

		if aux2.derecha != None:
			self.insertarF(nuevo,aux2)
		else:
			aux2.derecha = nuevo
			nuevo.izquierda = aux2
			print "se creo la info %s" %nuevo.info 
	aux1 = None
	aux2 = None 		

	def insertarC(self, nuevo, aux):
		aux = aux.abajo
		letra = aux.info[:1]
		nletra = nuevo.info[:1]
		if (ord(nletra) > ord(letra)):
			if aux.abajo != None:
				insertarC(nuevo, aux) 
			else:
				aux.abajo = nuevo
				nuevo.arriba = aux

		else:
			aux3 = aux.abajo
			nuevo.abajo = aux3
			#aux2.arriba = nuevo
			aux.abajo = nuevo
			#nuevo.arriba = aux
		print "se creo la info %s" %nuevo.info 
		aux =None
		return nuevo

	def insertarF(self, nuevo, aux):
		aux = aux.derecha
		letra = aux.info[:1]
		nletra = nuevo.info[:1]
		if (ord(nletra) > ord(letra)):
			if aux.derecha != None:
				nuevaCol(nuevo, aux) 
			else:
				aux.derecha = nuevo
				nuevo.izquierda = aux

		else:
			aux4=aux.derecha
			nuevo.derecha = aux4
			#aux2.izquierda = nuevo
			aux.derecha = nuevo
			#nuevo.izquierda = aux
		print "se creo la info %s" %nuevo.info 
		aux=None
			
	def buscarDom(self, ninfo):
		aux = self.cabeza
		b1 = False
		while b1 == False:
			while aux.derecha != None:
				aux = aux.derecha
				if (aux.info == ninfo):
					b1 = True
					print "se busca el dom %s" %aux.info
					break 
			if b1==False:
				print "No existe este dominio"
				b1 = True;
				return None

		contador = 0
		naux = aux.abajo
		while aux.abajo != None:
				aux = aux.abajo
				contador = contador + 1

		lista = [None] * contador

		for x in range(0,contador):
			lista[x] = naux.info
			naux = naux. abajo
			print lista[x]

		return lista

	def buscarLetra(self, ninfo):
		aux = self.cabeza
		b1 = False
		while b1 == False:
			while aux.abajo != None:
				aux = aux.abajo
				if (aux.info == ninfo):
					b1 = True
					print "se busca la letra %s" %aux.info
					break 
			if b1==False:
				print "No existe esta letra"
				b1 = True;
				return None

		contador = 0
		naux = aux.derecha
		while aux.derecha != None:
				aux = aux.derecha
				contador = contador + 1

		lista = [None] * contador

		for x in range(0,contador):
			lista[x] = naux.info
			naux = naux. derecha
			print lista[x]

		return lista

	def eliminar(self, nfila, ncol, dato):
		aux1 = self.cabeza
		aux2 = self.cabeza
		b1 = False
		b2 = False
		while b1 == False:
			while aux1.derecha != None:
				aux1 = aux1.derecha
				if (aux1.info == ncol):
					b1 = True
					print "encontro el dom %s" %aux1.info 
					break	
			if b1==False:
				asd = NodoMatriz(ncol)
				nuevaCol(asd, self.cabeza)
				b1 = True
				insertar(nfila, ncol, nuevo, ninfo)

		while b2 == False:
			while aux2.abajo != None:
				aux2 = aux2.abajo
				if (aux2.info == nfila):
					b2 = True
					print "encontro la letra %s" %aux2.info 
					break
			if b2==False:
				asd = NodoMatriz(nfila)
				nuevaFila(asd, self.cabeza)
				b2 = True
				insertar(nfila, ncol, nuevo, ninfo)
		
		aux3=aux1
		aux1 = aux1.abajo
		while dato != aux1.info:
			aux1 = aux1.abajo
			aux3 = aux3.abajo	


		aux3.abajo = aux1.abajo

		aux4=aux2
		aux2 = aux2.derecha
		while dato != aux2.info:
			aux2 = aux2.derecha
			aux4 = aux4.derecha	

		aux4.derecha = aux2.derecha

		print "eliminando %s" %aux2.info 

prueba = Matriz()
ex1 = NodoMatriz("gmail.com")
prueba.nuevaCol(ex1, None)
ex2 = NodoMatriz('a')
prueba.nuevaFila(ex2, None)
ex3 = NodoMatriz("hotmail.com")
prueba.nuevaCol(ex3, None)
ex4 = NodoMatriz('d')
prueba.nuevaFila(ex4, None)
ex5 = NodoMatriz("david")
prueba.insertar('d', "hotmail.com", ex5)
ex6 = NodoMatriz("ana")
prueba.insertar('a', "gmail.com", ex6)
ex7 = NodoMatriz("andres")
prueba.insertar('a', "hotmail.com", ex7)
ex8 = NodoMatriz('b')
prueba.nuevaFila(ex8, None)
#ex9 = NodoMatriz()
#ex9.setInfo("gmail.com")
prueba.buscarDom("gmail.com")
prueba.buscarLetra('a')
prueba.eliminar('d', "hotmail.com", "david")







