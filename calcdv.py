import sys
import re

# Tabla de valores
tabval = {
       'A':'14', 'B':'01', 'C':'00',
       'D':'16', 'E':'05', 'F':'20',
       'G':'19', 'H':'09', 'I':'24',
       'J':'07', 'K':'21', 'L':'08',
       'M':'04', 'N':'13', 'O':'25',
       'P':'22', 'Q':'18', 'R':'10',
       'S':'02', 'T':'06', 'U':'12',
       'V':'23', 'W':'11', 'X':'03',
       'Y':'15', 'Z':'17'
      }

# Dominios validos
# ABC123
# 123ABC
# 123ABCD
# A1234567
# AB123CD

# RegEx para validar el dominio
regexdom = re.match(r'^[A-Z]{3}[0-9]{3}$|^[0-9]{3}[A-Z]{3,4}$|^[A-Z][0-9]{7}$|^[A-Z]{2}[0-9]{3}[A-Z]{2}$', sys.argv[1])

# Crea una lista para procesar el dominio
def makelist(string):
    listareves = []
    for i in string:
        if i in tabval:
            listareves.append(int(tabval[i][:1]))
            listareves.append(int(tabval[i][1:]))
        else:
            listareves.append(int(i))
    listareves = listareves[::-1]
    return listareves


# Divide la lista de makelist() para poder calcular el digito verificador
def splitlist(listdv):
    ldv1 = listdv[::2]
    ldv2 = listdv[1::2]
    return ldv1, ldv2

# Checkea si el dominio es valido
if regexdom is None:
    print('[-] Dominio invalido')
    exit()

dom = makelist(sys.argv[1])
listadigito1, listadigito2 = splitlist(dom)
dv1 = sum(listadigito1)
dv2 = sum(listadigito2)
while(dv1 > 9):
    listadigito1 = makelist(str(dv1))
    dv1 = sum(listadigito1)
while(dv2 > 9):
    listadigito2 = makelist(str(dv2))
    dv2 = sum(listadigito2)

print("[+] El digito verificador de "+sys.argv[1]+" es "+str(dv1)+""+str(dv2))
