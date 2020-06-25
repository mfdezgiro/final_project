def folder_results():

	import shutil
	import os

	os.mkdir("blast_results")

	dest1 = "blast_results"

	files = os.listdir()

	for f in files:

		if f.startswith("blast_"):

	   		shutil.move(f, dest1)


	os.mkdir("muscle_results")

	dest2 = "muscle_results"

	files = os.listdir()

	for f in files:

		if f.startswith("muscle_"):

	   		shutil.move(f, dest2)



	os.mkdir("trees")

	dest3 = "trees"

	files = os.listdir()

	for f in files:

		if f.startswith("tree_"):

	   		shutil.move(f, dest3)


	os.mkdir("domains")

	dest4 = "domains"

	files = os.listdir()

	for f in files:

		if f.startswith("dominios_"):

	   		shutil.move(f, dest4)
