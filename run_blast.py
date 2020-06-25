def create_query():
	
	import sys

	file = open("my_query","a")
	with open(sys.argv[1]) as inputquery:
		file.write(inputquery.read()) #mismo texto que la query_input 

def blast():
	
	import os

	bl = "blastp -query my_query -subject my_multifasta -evalue 0.00001 -outfmt '6 qseqid qcovs pident sseqid sseq' -out my_blast"
	os.system(bl)


	
