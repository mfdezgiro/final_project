import shutil
import os

folders = ["blast_results", "muscle_results", "trees", "domains"]

for i in range(len(folders)):

	os.mkdir(folders[i])

	files = os.listdir()

	for f in files:

		if f.startswith(folders[i][0:4]):

	   		shutil.move(f, folders[i])
