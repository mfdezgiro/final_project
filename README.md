Usage:
"""
main.py input_file_query input_folder_genbanks coverage(optional) identity(optional)
""" 
Este programa busca proteínas query (concretamente PBPs) en genomas de organismos extremófilos.
Obtiene árboles filogenéticos que dan una pista sobre a cuál de esos organismos podría pertenecer.
Además obtiene todos los dominios.

El primer argumento debe ser un fasta (o multifasta) que contiene las querys. 

Se pueden definir opcionalmente los parámetros de coverage e identidad poniéndolos como tercer y cuarto argumento.

LOS IDENTIFICADORES DE LAS QUERYS DEBEN TENER 4 LETRAS
