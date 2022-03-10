
def leerdatos():
    fdatos= open("prevision.txt","r")
    vDatos=[]
    for linea in fdatos :
        vDatos.append(linea)
    fdatos.close()
    return vDatos


def contarsoleados(vDatos):
    for linea in vDatos :
        datos=linea.split("-")
        if datos[1]=="Soleado" or datos[1]=="Soleado\n":
            print("El dia", datos[0],"sera soleado")

def contarnieve(vDatos):
    for linea in vDatos:
        datos=linea.split("-")
        if datos[1]=="Nieve" or datos[1]=="Nieve\n":
             print("El dia", datos[0],"nevara y caeran ", datos[2], "de nieve")
        


vDatos=leerdatos()
print(vDatos)
soleados=contarsoleados(vDatos)
print(soleados)
nieve=contarnieve(vDatos)
print(nieve)

