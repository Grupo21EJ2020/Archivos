# este codigo copia un archivo

archivoorigen = open("./archivos/nuevo.txt","r",encoding='utf8')

archivodestino = open("./archivos/copia.txt","w",encoding='utf8')

archivodestino.write(archivoorigen.read())

archivoorigen.close()
archivodestino.close()