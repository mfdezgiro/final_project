
v1.0.0 -final project- Programming for Bioinformatics <br> 
Author: Miriam Fernández-Giro Muñoz <br><br>

Usage: main.py input_file_query input_folder_genbanks coverage(opt) identity(opt) <br><br>

Usage example: python3 main.py PBPs_query.fa genbanks <br>
(EXAMPLE FILE AND FOLDER INCLUDED IN THE REPOSITORY) <br><br>

Requirements: 

	sys.argv[1] must be a single fasta or multifasta file containing the queries. This file must be included in the working directory.
	IMPORTANT NOTE: query ID must have ONLY 4 LETTERS (e.g mrcB). 

	sys.argv[2] must be a single folder containing genbanks files. This folder must be included in the working directory.
	
	prosite.dat included in the working directory


Extra info about the project: initially used to find sequence homology by blastp between five PBPs (mrcB, mrdA, FtsI, pbpF, dacB) in eight genomes of extremophiles organisms. However it can be used to find homology between any query or queries in any genome (in genbank format) and create one phylogenetic tree for each query. <br>
Note: phylogenetic trees have no extension, user can add .nw if necessary <br> 
Default coverage value: 50 <br>
Default identity value: 25 <br>
Includes a module to find domains (using PROSITE) in each query together with the aligned part of the subject sequences <br>
IMPORTANT NOTE: DOES NOT search domains in proteins NOT present in the results of blastp

"""
