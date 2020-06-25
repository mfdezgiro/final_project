def muscle():
	import os

	mrcB_align = "muscle -in blast_mrcB -out muscle_mrcB"
	mrcB_tree = "muscle -maketree -in mrcB_muscle -out tree_mrcB -cluster neighborjoining"
	os.system(mrcB_align)
	os.system(mrcB_tree)

	mrdA_align = "muscle -in blast_mrdA -out muscle_mrdA"
	mrdA_tree = "muscle -maketree -in mrdA_muscle -out tree_mrdA -cluster neighborjoining"
	os.system(mrdA_align)
	os.system(mrdA_tree)

	FtsI_align = "muscle -in blast_FtsI -out muscle_FtsI"
	FtsI_tree = "muscle -maketree -in FtsI_muscle -out tree_FtsI -cluster neighborjoining"
	os.system(FtsI_align)
	os.system(FtsI_tree)

	pbpF_align = "muscle -in blast_pbpF -out muscle_pbpF"
	pbpF_tree = "muscle -maketree -in muscle_pbpF -out tree_pbpF -cluster neighborjoining"
	os.system(pbpF_align)
	os.system(pbpF_tree)

	dacB_align = "muscle -in blast_dacB -out dacB_muscle"
	dacB_tree = "muscle -maketree -in muscle_dacB -out tree_dacB.nw -cluster neighborjoining"
	os.system(dacB_align)
	os.system(dacB_tree)

def move_muscle():

	import shutil
	import os

	if not os.path.exists("muscle_results"):
		os.mkdir("muscle_results")

	dest2 = "muscle_results"

	files = os.listdir()

	for f in files:
		if f.startswith("muscle_"):
	   	 shutil.move(f, dest2)

def move_trees():

	import shutil
	import os

	if not os.path.exists("trees"):
		os.mkdir("trees")

	dest3 = "trees"

	files = os.listdir()

	for f in files:
		if f.startswith("tree_"):
	   	 shutil.move(f, dest3)
