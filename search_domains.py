def domains():
	import re
	from Bio.ExPASy import Prosite,Prodoc
	import os

	handle = open("prosite.dat","r")
	records = Prosite.parse(handle)
	lectura="" 

	for archivo in os.listdir():

		if archivo.startswith("blast_") == True:

			dominios = open("domains_"+archivo,'a')
			dominios.write("lista de dominios en proteinas de "+archivo+":\n")

	for linea in records:

		name = linea.name
		accession = linea.accession
		description = linea.description
		pattern = linea.pattern
		pattern = pattern.replace('{', '[^')
		pattern = pattern.replace('}', ']')
		pattern = pattern.replace('(', '{')
		pattern = pattern.replace(')', '}')
		pattern = pattern.replace('-', '')
		pattern = pattern.replace('x', '.')
		pattern = pattern.replace('>', '$')
		pattern = pattern.replace('<', '^')
	
		for archivo in os.listdir():
			#busca los dominios en cada archivo multifasta obtenido en el filtrado del blast 
			if archivo.startswith("blast_") == True:	
					
				query = open(archivo, 'r')
				lectura = query.read()
				dominios = open("domains_"+archivo,'a') #vuelve a abrir cada archivo creado anteriormente
			

				if re.search(pattern, lectura):

					if not pattern == "":
				
						dominios.write("encontrado dominio de: "+name+" con accession: "+accession+" y description: "+description+" cuyo patrón es "+pattern+"\n")

	
