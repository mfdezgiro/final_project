def create_query():
	
	import sys
	
	#lee el input_query y guarda su contenido en un nuevo archivo llamado my_query
	file = open("my_query","a")
	with open(sys.argv[1]) as inputquery:
		file.write(inputquery.read())  

def blast():
	
	import os

	bl = "blastp -query my_query -subject my_multifasta -evalue 0.00001 -outfmt '6 qseqid qcovs pident sseqid sseq' -out my_blast"
	os.system(bl)


	
