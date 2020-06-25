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


Extra info about the project: initially used to find sequence homology by blastp between five PBPs (mrcB, mrdA, FtsI, pbpF, dacB) in eight genomes of extremophiles organisms. However it can be used to find homology between any query or queries in any genome (in genbank format).
Default coverage value: 50
Default identity value: 25
Includes a module to find domains (using PROSITE) in each query together with the aligned part of the subject sequences
IMPORTANT NOTE: DOES NOT search domains in proteins NOT present in the results of blastp


"""

import genbanks_parse
import os
import run_blast
import filter_and_muscle
import search_domains
import move_results

genbanks_parse.parseo()
os.chdir("..")

run_blast.create_query()
run_blast.blast()

filter_and_muscle.muscle()

search_domains.domains()

move_results.folder_results()



