
# Practica 3 Teoria Computacional
#
# Alumno: Mohedano Monter Eduardo
#
# Grupo: 2CV5
#
# Descripcion: Hacer un Automata Finito Determinista que reconozaca palabras del lenguaje dado por la expresion regular a+bc*
# 


# Sea la matriz que almacena la tabla de transiciones dada por:

#    a b c
# Q0 x x x
# Q1 x x x 
# Q2 x x x 
# E  x x x 

matrizTransiciones = [
						["Q1","E" ,"E" ],
						["Q1","Q2","E" ],
						["Q1","E" ,"Q2"],
						["E" ,"E" ,"E" ],					
					]
# el diccionario de simbolos es el alfabeto (VT)
diccionarioSimbolos = {"a":0,"b":1,"c":2}

# el diccionario de estados son todos los posibles estados a los que puede llegar un automata
diccionarioEstados = {"Q0":0,"Q1":1,"Q2":2,"E":3}	

# arreglo con los estados de aceptacion
estadosDeAceptacion= ["Q2"]

estadoInicial = "Q0";


palabra = raw_input("Introduzca una palabra que pertenezca al alfabeto E={"+",".join(diccionarioSimbolos.keys())+"} y que cumpla con la expresion a+bc*\n")


estadoActual = estadoInicial

index = 0

# se recorre la cadena caracter a caracter mientras no se llegue al estado de error
while index < len(palabra) and estadoActual != "E":
	
	simbolo = palabra[index]
	
	# si el simbolo no pertenece al alfabeto dejamos de recorrer la palabra
	if not diccionarioSimbolos.has_key(simbolo):
		estadoActual = "E"
		break
		
	print "Estado Actual:"+estadoActual+"\tSimbolo: "+simbolo
	
	# consultamos las posiciones asociadas a cada estado dentro de las filas de la matriz de tranciciones
	posEstadoActual = diccionarioEstados[estadoActual]
	
	# consultamos las posiciones asociadas a cada simbolo dentro de las columnas de la matriz de tranciciones
	posSimboloActual = diccionarioSimbolos[simbolo]
	
	# se obtienen el siguiente estado usando la matriz de tranciciones
	estadoActual = matrizTransiciones[posEstadoActual][posSimboloActual]
		
	index += 1


if estadosDeAceptacion.__contains__(estadoActual):
	print "\nLa cadena "+palabra+" pertenece al lenguaje generado por a+bc*"
else:
	print "\nLa cadena "+palabra+" NO pertenece al lenguaje generado por a+bc*"

