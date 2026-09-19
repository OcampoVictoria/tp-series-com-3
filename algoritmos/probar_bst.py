from estructuras.arbol_binario import ArbolBST

class Elemento:
    def __init__(self, titulo, genero):
      self.titulo = titulo
      self.genero = genero

    def __repr__(self):
      return f"{self.titulo} (genero {self.genero})"
    
def main():
    arbol = ArbolBST()
# Lo construimos SIN orden, para que el árbol ordene solo
    datos = [
           Elemento("Pinnochio", "Romance"),
           Elemento("W: two Worlds", "Fantasia"),
           Elemento("Doctor Stranger", "Melodrama"),
           Elemento("Romance is a Bonus Book", "Romance"),
           Elemento("I Hear You Voice", "Fantasia"),
    ]
    for d in datos:
      arbol.insertar(d, clave=lambda e: e.titulo.lower())

    print("Altura del árbol:", arbol.altura())

    print("\n--- inorder (ordenado alfabéticamente) ---")
    for e in arbol.inorder():
     print(" ", e)

    print("\n--- preorder ---")
    for e in arbol.preorder():
     print(" ", e.titulo)

    print("\n--- postorder ---")
    for e in arbol.postorder():
      print(" ", e.titulo)

    print("\n--- búsquedas ---")
    encontrado = arbol.buscar("pinnochio", clave=lambda e: e.titulo.lower())
    print("Buscar 'Pinnochio':", encontrado)
    no_encontrado = arbol.buscar("zzz", clave=lambda e: e.titulo.lower())
    print("Buscar 'zzz':", no_encontrado)

if __name__ == "__main__":
 main()

