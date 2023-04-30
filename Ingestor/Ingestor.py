#Ingestor para los datos de los disdrometros
import os
import datetime
import shutil

base_dir = "./"
data_dir = base_dir + "converted_data/"
raw_data_dir = base_dir + "raw_data/"
backup_dir = base_dir + "backup_data/"

#se crea la carpeta donde se guardaran los archivos convertidos en formato dd-mm-aaaa y una carpeta para los archivos originales
today = datetime.date.today()
today = today.strftime("%d-%m-%Y")
converted_data_dir = data_dir + "data_" + today
backup_data_dir = backup_dir + "data_" + today
#si no existe la carpeta se crea
if not os.path.exists(converted_data_dir):
    os.makedirs(converted_data_dir)
if not os.path.exists(backup_data_dir):
    os.makedirs(backup_data_dir)

#se abren los archivos de raw_data_dir uno a uno
for filename in os.listdir(raw_data_dir):
    #se lee el archivo
    with open(raw_data_dir + filename, 'r') as file:        
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
            resultado = f"{parsed_raw};\n{I};{P};{Z};{St};{N};{Tsensor};{Tsgr};{Tshl};{Hc};{timestamp};\n"
           
            # Se escribe el string final en el archivo
            with open(converted_data_dir + "/Data-" + today + ".txt", 'a') as f:
                f.write(resultado)
                f.close()   
    

    #se mueve el archivo a la carpeta backup excepto el archivo .gitkeep
    if filename != ".gitkeep":
        shutil.move(raw_data_dir + filename, backup_data_dir + "/" + filename)

    
        
   







