import os
import time
os.system(" ")


colorVerde = "\033[0;32;40m"
colorBlanco = "\033[0;37;40m"
colorRojo = "\033[0;31;40m"
def cambiaColor(color):
    print(color, end="")



def separarRegistros(cadena, separador):
    registros=[]
    registro=""
    for letra in cadena:
        if separador not in letra and letra != "\n":
            registro+=letra
        else:
            registros.append(registro)
            registro=""
    if letra != "\n":
        registros.append(registro)
    return registros



def corregirIPv6(ip):
    correccion = ""
    for letra in ip:
        if "/" in letra:
            return correccion
        correccion += letra
    return correccion




def formatoDecimalIPv6(ip):
    formatodec = ""
    for i in range(len(ip)):
        formatodec += str(int(ip[i], 16))
        if i != len(ip)-1:
            formatodec+=":"
    return formatodec



def formatoHexadecimalIP(ip):
    formatohexa = ""
    for i in range(len(ip)):
        formatohexa += str("{0:02x}".format(int(ip[i]))).upper()
        if i != len(ip)-1:
            formatohexa+="."
    return formatohexa




def convertirDatos(linea):
    registros = separarRegistros(linea, ",")
    #Comprobacion de formato
    if len(registros) != 6:
        cambiaColor(colorRojo)
        print("Se encontró un formato erroneo")
        cambiaColor(colorBlanco)
        return;
    #Conversion a decimal de la ipv6
    salida = registros.copy()
    salida[0] = corregirIPv6(salida[0])
    ipv6vals = separarRegistros(salida[0], ":")
    salida[0] = formatoDecimalIPv6((ipv6vals))
    #Reacomodo de 2da cadena y eliminacion de las demas cadenas
    salida.insert(0, salida[2])
    salida.pop(2)
    salida.pop(2)
    salida.pop(2)
    salida.pop(2)
    #Conversion de ip a hexadeximal
    ipvals = separarRegistros(salida[2], ".")
    salida[2] = formatoHexadecimalIP(ipvals)
    cambiaColor(colorBlanco)
    print(registros)
    time.sleep(.2)
    cambiaColor(colorVerde)
    print(salida)


archivo = open("datos.txt", "r")
datos = archivo.readlines()
for dato in datos:
    convertirDatos(dato)
    print("")
    
input()