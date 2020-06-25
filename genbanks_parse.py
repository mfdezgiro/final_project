""" This script obtains a multifasta file with all the CDS in all the input genbanks """

import os
import sys
from Bio import Seq, SeqIO

input_genbanks = sys.argv[2]

def parseo():

    f = open("my_multifasta","a") #crea el archivo que va a contener todas las proteínas de todos los genbanks
    os.chdir(input_genbanks)

    for gbks in os.listdir():

        if os.path.isfile(gbks) == True:

            with open(gbks, "r") as input_handle:
        
                for record in SeqIO.parse(input_handle, "genbank"):
        
                    for feature in record.features:
            
                        if feature.type == 'CDS':

                            try:
                                seqprot = feature.qualifiers['translation'][0]
                    
                            except:
                                seqprot = "empty"
             
                            if seqprot != "empty":
				#para poner también en la cabecera el nombre de la especie con el formato n_especie
                                nombre = record.description.split(" ")  
                                n_especie = nombre[0][0]+"_"+nombre[1]

                                f.write(">"+feature.qualifiers['locus_tag'][0]+"_"+n_especie+"\n"+seqprot+"\n")

                         

                
                    
    
