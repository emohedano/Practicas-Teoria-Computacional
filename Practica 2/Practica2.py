 #!/usr/bin/python

# Practica 2 de Teoria Computacional
# 
# Alumno: Mohedano Monter Eduardo
# 
# Grupo: 2CV5
# 
# Descripcion: Se debe generar un reporte (reporte.txt) de cuantas veces 
# esta contenida cada palabra de la lista (palabras.txt) en el texto (texto.txt) 

texto = open("texto.txt")
palabrasBuscadas = open("palabras.txt")
reporte = open ("reporte.txt", "w")

#se leen las palabras que seran buscadas
palabrasBuscadas = palabrasBuscadas.readlines()

#se lee el cuerpo del texto
cadenaTexto  = texto.read()

# quitamos los saltos de linea y los espacios dobles
listaPalabrasTexto = cadenaTexto.replace("\n"," ").replace("  "," ").split(" ")

# se ordenan las palabras del texto en orden alfabetico
listaPalabrasTexto.sort()
 
i=0
j=0
veces=0

print "Generando reporte..."

#se recorre la lista de las palabras buscadas
while i < len(palabrasBuscadas):
    
    palabraBuscada = palabrasBuscadas[i].replace("\n","")
    
    #se compara la palabra buscada con cada palabra del texto    
    while j < len(listaPalabrasTexto):
        
        palabraActual = listaPalabrasTexto[j]
    	
        posicion = 0
        index = 0
        seguir = True
        
        #recorremos caracter por caracter de la palabra actual
        while index < len(palabraActual) and seguir:
            
            #si el caracter es alfanumerico 
            if palabraActual[index].isalpha() :
                
                #se recorre caracter por caracter de dichas palabras hasta que los caracteres no coincidan 
                while index < len(palabraActual) and posicion < len(palabraBuscada) and palabraActual[index] == palabraBuscada[posicion]:
                    
                    index += 1 
                    posicion += 1
                
                # si el numero de posicion es igual a la longitud de la palabra buscada
                # entonces la palabra actual contiene a la palabra buscada    
                if posicion == len(palabraBuscada) and ( index == len(palabraActual) or not palabraActual[index].isalpha()):
                    veces += 1
                
                seguir = False
                
            else:
                index += 1    
            		
        j += 1

    
    #se guarda la palabra buscada y las veces que aparece en el texto
    reporte.write(palabrasBuscadas[i].replace("\n","")+" : "+ str(veces)+"\n")
        
    veces = 0
    j = 0
    i += 1

reporte.close()

print "Abriendo reporte...\n"

reporte = open ("reporte.txt")

print reporte.read()
    
