import sys
import re

# Tabla de valores
wtf = {
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

# RegEx para validar el dominio
regexpat = re.match(r'^[A-Z]{3}[0-9]{3}$|^[0-9]{3}[A-Z]{3,4}$|^[A-Z][0-9]{7}$|^[A-Z]{2}[0-9]{3}[A-Z]{2}$', sys.argv[1])

# Crea una lista para procesar el dominio
def makelist(string):
    listareves = []
    for i in string:
        if i in wtf:
            listareves.append(int(wtf[i][:1]))
            listareves.append(int(wtf[i][1:]))
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
if regexpat is None:
    print('[-] Dominio invalido')
    exit()

pat = makelist(sys.argv[1])
listaDigito1, listaDigito2 = splitlist(pat)
dv1 = sum(listaDigito1)
dv2 = sum(listaDigito2)
while(dv1 > 9):
    listaDigito1 = makelist(str(dv1))
    dv1 = sum(listaDigito1)
while(dv2 > 9):
    listaDigito2 = makelist(str(dv2))
    dv2 = sum(listaDigito2)

print("[+] El digito verificador de "+sys.argv[1]+" es "+str(dv1)+""+str(dv2))
