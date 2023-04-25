#Ingestor para los datos de los disdrometros

#Tutorial
# Para convertir archivos se debe borrar todo el contenido de la carpeta raw_data y colocar alli los archivos a convertir
# Luego se debe ejecutar el script y se creará automaticamente dentro de la carpeta converted_data una carpeta llamada data_FechaDeHoy con los archivos convertidos 
# Para ejecutar el script se debe ejecutar alguno de los siguientes comandos en la terminal: 
# python Ingestor.py
# python3 Ingestor.py
# py Ingestor.py

import os
import datetime
import time
import shutil

base_dir = "./"
data_dir = base_dir + "converted_data/"
raw_data_dir = base_dir + "raw_data/"

#se crea la carpeta donde se guardaran los archivos convertidos en formato dd-mm-aaaa
today = datetime.date.today()
today = today.strftime("%d-%m-%Y")
converted_data_dir = data_dir + "data_" + today
#si no existe la carpeta se crea
if not os.path.exists(converted_data_dir):
    os.makedirs(converted_data_dir)
#se abre el archivo converted_data_dir y se escribe en él los datos convertidos

#se abren los archivos de raw_data_dir uno a uno
for filename in os.listdir(raw_data_dir):
    #se lee el archivo
    with open(raw_data_dir + filename, 'r') as file:
        #se imprime el contenido del archivo
        #print(file.read())
        #lee linea a linea
        for line in file:
        # Dividir la línea en elementos utilizando ":" como delimitador
            elementos = line.split(":")

            # Obtener los valores solicitados
            elementos = line.split()
            timestamp = elementos[0]
            N = elementos[1].split(":")[0]
            Tsensor = elementos[1].split(":")[1]
            Tsgr = elementos[1].split(":")[2]
            Tshl = elementos[1].split(":")[3]
            Hc = elementos[1].split(":")[4]
            I = elementos[1].split(":")[5]
            P = elementos[1].split(":")[6]
            Z = elementos[1].split(":")[7]
            St = elementos[1].split(":")[8]
            raw = ":".join(elementos[1:]).split(":")[9]

            # Se concatena cada 3 caracteres del elemento "raw" con ";"
            parsed_raw = ';'.join([raw[i:i+3] for i in range(0, len(raw), 3)])

            # Se arma el string final
            resultado = f"{parsed_raw}\n{I};{P};{Z};{St};{N};{Tsensor};{Tsgr};{Tshl};{Hc};{timestamp};\n"
           
            # Se escribe el string final en el archivo
            with open(converted_data_dir + "/" + filename, 'a') as file:
                file.write(resultado)
                file.close()







