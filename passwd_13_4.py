#!/usr/bin/python

# Nerea Del Olmo Sanz - GITT
# Ejercico 13.4


pass_file = open ("/etc/passwd", "r")

file_lines = pass_file.readlines()  # guarda cada linea como un elemento de la lista

for line in file_lines:
	conf = line.split(":") 	        # Busca : en la cadena
	user = conf [0] 			    # Se queda con el primer elemento
	shell = conf [-1]			    # Se queda con el ultimo elemento
	print user, shell

users_number = len(file_lines)
print "There are " + str(users_number) + " users."

pass_file.close()
