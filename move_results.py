def folder_results():
	import shutil
	import os

	if not os.path.exists("blast_results"):
		os.mkdir("blast_results")

	dest1 = "blast_results"

	files = os.listdir()

	for f in files:
		if f.startswith("blast_"):
	   	 shutil.move(f, dest1)


	if not os.path.exists("muscle_results"):
		os.mkdir("muscle_results")

	dest2 = "muscle_results"

	files = os.listdir()

	for f in files:
		if f.startswith("muscle_"):
	   	 shutil.move(f, dest2)



	if not os.path.exists("trees"):
		os.mkdir("trees")

	dest3 = "trees"

	files = os.listdir()

	for f in files:
		if f.startswith("tree_"):
	   	 shutil.move(f, dest3)


	if not os.path.exists("domains"):
		os.mkdir("domains")

	dest4 = "domains"

	files = os.listdir()

	for f in files:
		if f.startswith("dominios_"):
	   	 shutil.move(f, dest4)
