"""
v1.0.0 -final project- Programming for Bioinformatics
Author: Miriam Fernández-Giro Muñoz

Usage: main.py input_file_query input_folder_genbanks coverage(opt) identity(opt)

Usage example: python3 main.py PBPs_query.fa genbanks 
(EXAMPLE FILE AND FOLDER INCLUDED IN THE REPOSITORY)

Requirements: 

	sys.argv[1] must be a single fasta or multifasta file containing the queries. This file must be included in the working directory.
	IMPORTANT NOTE: query ID must have ONLY 4 LETTERS (e.g mrcB). 

	sys.argv[2] must be a single folder containing genbanks files. This folder must be included in the working directory.

"""

import genbanks_parse
import os
import run_blast
import filter_and_muscle
import search_domains
import move_results

genbanks_parse.parseo()
os.chdir("..")
print("Obtenido el multifasta con todas las CDS\n")

run_blast.create_query()
run_blast.blast()
print("Blastp hecho!\n")

filter_and_muscle.muscle()
print("\nAlineamiento con muscle hecho!\n")

search_domains.domains()
print("Dominios encontrados!\n")

move_results.folder_results()
print("Done!\nConsulta los resultados del trabajo en las carpetas creadas\n")



