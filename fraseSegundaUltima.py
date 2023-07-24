frase ="El perro del Rayo no tiene rabo"
contador=0
contadorInicio=1;
contadorFin=1;

for f in frase:
    contador=contador+1
    if f== " ":
        contadorInicio=contador;
        break;
contador=0
for f in frase:
    contador=contador+1
    if f== " ":
        contadorFin=contador-1;
        
print(frase[contadorInicio:contadorFin])       
    