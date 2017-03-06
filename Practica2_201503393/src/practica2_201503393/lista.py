#from flask import Flask, request, Response
#app = Flask("Practica2")

class NodoLista:
	#derecha = NodoMatriz("")
	#izquierda = NodoMatriz("")
	#abajo = NodoMatriz("")
	#arriba = NodoMatriz("")
	#info = ""
	print "Funciona"

	def __init__(self, info):
		self.info = info
		self.abajo= None

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

class Lista:

	def __init__(self):
		self.cabeza = NodoLista("0")

	def nuevaFila(self, nuevo, aux):
		if aux == None:
			aux=self.cabeza
		if self.cabeza.abajo == None:
			self.cabeza.abajo=nuevo
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
				aux.abajo = nuevo
				print "se creo la letra %s" %nuevo.info 

	#contadorf = 0
	#contadorc= 0
	
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

	def eliminar(self, ninfo):
		pass

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







