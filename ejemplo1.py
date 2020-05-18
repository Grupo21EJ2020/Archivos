#este programa lee el contenido de un archivo.
# lo imprime por linea y muestra la longitud de la 
#linea

archivo = open("./archivos/nuevo.txt",'r',encoding='utf8')

for renglon in archivo:
    print(f'Datos del renglon:{renglon}No.Caract. {len(renglon)}')

archivo.close()