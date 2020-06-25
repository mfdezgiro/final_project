
v1.0.0 -final project- Programming for Bioinformatics <br> 
Author: Miriam Fernández-Giro Muñoz <br><br>

Usage: 

	python3 main.py input_file_query input_folder_genbanks coverage(opt) identity(opt) 

Usage example: 
	
	python3 main.py PBPs_query.fa genbanks
	
(EXAMPLE FILE AND FOLDER INCLUDED IN THE REPOSITORY) <br><br>

Requirements: (READ CAREFULLY BEFORE USE) 

	input_file_query (= sys.argv[1]) 
must be a single fasta or multifasta file containing the queries. This file must be included in the working directory. <br>
	IMPORTANT NOTE: query ID must have ONLY 4 LETTERS (e.g mrcB) due to the internal processing of the files.

	input_folder_genbanks (= sys.argv[2])
must be a single folder containing genbanks files. This folder must be included in the working directory. <br>
One extra file:
	
	prosite.dat 
must be included by the user in the working directory. <br> <br>


Extra info about the project: initially used to find sequence homology by blastp between five PBPs (mrcB, mrdA, FtsI, pbpF, dacB) in eight genomes of extremophiles organisms. However it can be used to find homology between any query or queries in any genome (in genbank format) and create one phylogenetic tree for each query. <br>
Note: phylogenetic trees have no extension, user can add .nw if necessary <br> 
Default coverage value: 50 <br>
Default identity value: 25 <br>
Includes a module to find domains (using PROSITE) in each query together with the aligned part of the subject sequences <br>
IMPORTANT NOTE: DOES NOT search domains in proteins NOT present in the results of blastp <br> <br>

FINAL NOTE: Only one use per project (folder results are created only once). If wished to do another analysis, take out:
	
	my_multifasta
	my_query
	my_blast
	blast_results
	muscle_results
	trees
	domains
	
from the working directory.


