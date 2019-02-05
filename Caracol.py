def cargar_archivo(lab):
    ##return [x.split(" ") for x in [y.strip("\n") for y in open(lab).readlines()]]
    return open(lab)

def moverDer(mat,fil,col,aux,tam):
    if(tam>0):
        if(aux<tam):
            print(mat[fil][col],end=" ")
            moverDer(mat,fil,col+1,aux+1,tam)
        if(aux==tam):
            moverAba(mat,fil+1,col-1,0,tam-1)
    else:
        print("Termino")

def moverAba(mat,fil,col,aux,tam):
    if(tam>0):
        if(aux<tam):
            print(mat[fil][col],end=" ")
            moverAba(mat,fil+1,col,aux+1,tam)
        if(aux==tam):
            moverIzq(mat,fil-1,col-1,0,tam)
    else:
        print("Termino")
def moverIzq(mat,fil,col,aux,tam):
    if(tam>0):
        if(aux<tam):
            print(mat[fil][col],end=" ")
            moverIzq(mat,fil,col-1,aux+1,tam)
        if(aux==tam):
            moverArr(mat,fil-1,col+1,0,tam-1)
    else:
        print("Termino")
        
def moverArr(mat,fil,col,aux,tam):
    if(tam>0):
        if(aux<tam):
            print(mat[fil][col],end=" ")
            moverArr(mat,fil-1,col,aux+1,tam)
        if(aux==tam):
            moverDer(mat,fil+1,col+1,0,tam)
    else:
        print("Termino")

def crear_mat(mat,lab):
    for x in cargar_archivo(lab):
        mat.append(x.strip().split())
    return mat

def leer_mat(mat,lab,col,fil):
    print(mat [col][fil])
        
def resolver(lab):
    moverDer(crear_mat([],lab),0,0,0,len(crear_mat([],lab)))
    
          
resolver("cara.txt") 


