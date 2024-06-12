def listar_inversa(recolección):
    if len(recolección) == 0:
        return
    
    contenido = recolección[0]
    listar_inversa(recolección[1:])
    
    print(contenido)


muestra = [1, 2, 3, 4, 5]
listar_inversa(muestra)


