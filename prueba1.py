prendas = {}
bodega = {}

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por categoría")
    print("2. Búsqueda de prendas por rango de precio")
    print("3. Actualizar precio de prenda")
    print("4. Agregar prenda")
    print("5. Eliminar prenda")
    print("6. Salir")
    print("=====================================")

def elegir_opcion():
   seguir = True
   while seguir:
      try:
         opcion = int(input("ingrese opcion:"))
         if 1 <= opcion <= 6:
            seguir = False
         else:
            print("==opcion fuera de rango==")
      except:
         print("opcion invalida debe ser valor entero positivo")
   return opcion


def buscar_codigo(codigo, bodega):
   codigo = codigo.upper()

   for cod in bodega:
      if cod.upper() == codigo:
         return True
   return False
      

def unidades_categoria(categoria, prendas, bodega):
   total = 0
   encontrada = False

   for codigo in prendas:
      if prendas[codigo][1].lower() == categoria.lower():
         total += bodega[codigo][1]
         encontrada = True

   if encontrada:
      print("El total de unidades es", total)
   else:
      print("no hay prendas registradas en esa categoria")


def busqueda_precio(p_minimo, p_maximo, prendas, bodega):

   lista = []

   for codigo in bodega:
      precio = bodega[codigo][0]
      unidades = bodega[codigo][1]

      if precio >= p_minimo and precio <= p_maximo and unidades > 0:
         nombre = prendas[codigo][0]
         lista.append(nombre + "--" + codigo)

   lista.sort()

   if len(lista) == 0:
      print("no hay prendas en ese rango de precios.")
   else:
      print("las prendas encontradas son:", lista)


def actualizar_precio(codigo, nuevo_precio, bodega):
   if buscar_codigo(codigo, bodega):
      codigo = codigo.upper()
      bodega[codigo][0] = nuevo_precio
      return True
   else:
      return False
   

def agregar_prenda(codigo, nombre, categoria, talla, color, material, es_unisex, precio, unidades, prendas, bodega):
   if buscar_codigo(codigo, bodega):
      return False
   codigo = codigo.upper()
   prendas[codigo] = [nombre, categoria, talla, color, material, es_unisex]
   bodega[codigo] = [precio, unidades]
   return True
       
def eliminar_prenda(codigo, prendas, bodega):
   if buscar_codigo(codigo, bodega):
      codigo = codigo.upper()
      del prendas[codigo]
      del bodega[codigo]
      return True
   else:
      return False
      

# programa principal 

prendas = {
    'S001': ['Polera Basica', 'polera', 'M', 'negro', 'algodon', True],
    'S002': ['Jeans Slim', 'pantalon', 'L', 'azul', 'denim', False],
    'S003': ['Chaqueta Urban', 'chaqueta', 'M', 'gris', 'poliester', True],
    'S004': ['Vestido Sol', 'vestido', 'S', 'rojo', 'lino', False],
    'S005': ['Poleron Cozy', 'poleron', 'XL', 'verde', 'algodon', True],
    'S006': ['Camisa Formal', 'camisa', 'M', 'blanco', 'algodon', False],  
}

bodega = {
    'S001': [7990, 12],
    'S002': [19990, 0],
    'S003': [29990, 3],
    'S004': [24990, 6],
    'S005': [17990, 8],
    'S006': [14990, 2],
}

opcion = 0
while opcion != 6:
   mostrar_menu()
   opcion = elegir_opcion()
   match opcion:
      case 1:
        categoria = input("ingrese categoria: ")
        print(categoria)
        unidades_categoria(categoria, prendas, bodega)
        
      case 2:
          valido = False
          while not valido:
             try:
                p_minimo = int(input("ingrese precio minimo: "))
                p_maximo = int(input("ingrese precio maximo: "))

                if p_minimo >= 0 and p_maximo >= 0 and p_minimo <= p_maximo:
                   valido = True
                else:
                   print("los valores son invalidos")
             except:
                print("ingrese valores enteros")
          busqueda_precio(p_minimo, p_maximo, prendas, bodega)
          
      case 3:
         respuesta = "s"

         while respuesta.lower() == "s":

            codigo = input("ingrese codigo de la prenda: ")

            valido = False
            while not valido:
               try:
                  nuevo_precio = int(input("ingrese nuevo precio: "))
                  if nuevo_precio > 0:
                     valido = True
                     if actualizar_precio(codigo, nuevo_precio, bodega):
                        print("Precio Actualizado")
                        respuesta = input("desea actualizar otro precio (s/n)?: ").lower()
                     else:
                        print("EL codigo no existe")
                  else:
                     print("debe ingresar un precio mayor que cero.")
               except:
                  print("debe ingresar numero entero")
      case 4:
         codigo = input("ingrese codigo: ")
         if not buscar_codigo(codigo, bodega):
           nombre = input("ingrese nombre: ")
           categoria = input("ingrese categoria: ")
           talla = input("ingrese talla: ")
           color = input("ingrese color: ")
           material = input("ingrese material: ")
           unisex = input("es unisex? (s/n): ").lower()
           es_unisex = unisex == "s"
           try:
             precio = int(input("ingrese precio: "))
             unidades = int(input("ingrese unidades "))

             if agregar_prenda(codigo, nombre, categoria, talla, color, material, es_unisex, precio, unidades, prendas, bodega):
                print("prenda agregada")
             else:
                print("el codigo ya existe")
           except:
              print("el precio o unidades debe ser numericos enteros")
         else:
            print("el codigo ya existe")

      case 5:
         codigo = input("ingrese codigo de la prenda: ")
         if eliminar_prenda(codigo, prendas, bodega):
            print("prenda eliminada")
         else:
            print("codigo no existe")
      case 6:
         print("Gracias por usar el programa")