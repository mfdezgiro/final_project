def muscle():
	import os
	import sys
	from Bio import SeqIO

	#añadir cada query en cada archivo blast_ correspondiente
	with open("my_query", "r") as queries:

		for record in SeqIO.parse(queries, "fasta"):
			arc = open("blast_"+record.id, "a")
			arc.write(">"+record.id+"\n"+str(record.seq)+"\n")

	#añadir los resultados del blast a cada query por separado
	with open("my_blast") as mf:
		lines = mf.readlines() 

	for i in range(len(lines)):

		id_ = lines[i][0:4]
		sseq = lines[i][14::]
		cov = lines[i][5:7]
		ident = lines[i][8:10]
		lista_ids = []
	
		for names in id_:
			lista_ids.append(id_)

		if len(sys.argv) == 5:
			valor_cov = sys.argv[3]
			valor_ident = sys.argv[4]
		else:
			valor_cov = "50"
			valor_ident = "25"
		

		if cov > valor_cov and ident > valor_ident:

			blast_files = open("blast_"+lista_ids[0], "a") #vuelve a usar el archivo de blast para cada query
			blast_files.write(">"+sseq.replace("\t","\n"))


	#ejecuta el muscle en cada archivo creado
	for archivo in os.listdir():
		if archivo.startswith("blast_") == True:
		
			align = "muscle -in %s -out muscle_%s" % (archivo, archivo)
			tree = "muscle -maketree -in muscle_%s -out tree_%s -cluster neighborjoining" % (archivo, archivo)
			os.system(align)
			os.system(tree)



