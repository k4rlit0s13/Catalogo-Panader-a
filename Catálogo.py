

#crear nuestra información completa y detallada, en este caso 3 categorías con 3 promociones cada una
#crear código que muestre, deje seleccionar, muestre valor, deje contar cuanto dinero, de vueltos y deje comprar promociones



#Diccionario: bloque que retendrá toda nuestra información
menu= dict({

#categorías(En Python, cuando defines un diccionario, cada par clave-valor debe estar separado por una coma ,)
#dentro de la categoria asignaremos una variable de producto como lista

#ahora agregamos la info dentro de estas para tener pares de Clave-Valor
#Dentro de las claves-valor irá la información del nombre del producto-precio del producto.(números no llevan comillas doblres por ser valores numéricos)
#Categoria CERO
    #ahora agregar como segunda lista acompañando la categoría Dulces son las Promociones, ATENCIÓN la misma categoria tiene 2 listas de la siguiente manera = nombre diccionario=dict({ "nombrelista":list{["":""]}, "nombrelista":list{["":""]} }) esto son 2 listas dentro de un diccionario separadas por una coma
    #con la info anterior entonces podemos empezar a llenar la lista principal(categoría) con su respectiva secundaria(promociones), el orden es(ojo esto es dentro ya del diccionario)= "nombre categoria":{ "productos"{[{""":""}]}, "promociones"{[{"":""}]} } las llaves son la clave para saber que los productos y las promociones son específicamente de la categoría "nombrecategoría"
    "Dulces": {
        "producto":list ([ {"nombre":"Croissants", "valor":3500},{"nombre": "Donas", "valor":2000},{"nombre": "Pastelitos", "valor":1500},{"nombre":"Galletas", "valor":7000},{"nombre":"Pan dulce","valor":5000},{"nombre":"Ensaimadas", "valor":6000},{"nombre":"Tartaletas", "valor":4500},{"nombre":"Bizcochos", "valor":2500},{"nombre":"Palmeras", "valor":2000},{"nombre":"Conchas", "valor":2000}]) , "Promociones":list ([ {"indice":0,"nombre":"Descuento del 5% por comprar 5 unidades de pan","unidades":5, "descuento": 0.05} , {"indice":0,"nombre":"Descuento del 7% por comprar 10 unidades","unidades":5, "descuento": 0.05} ]) },     
#categoria UNO
    "Salados": {"producto": list([{"nombre":"Baguettes", "valor":5000},{"nombre":"Pan de masa madre","valor":6000},{"nombre":"Pan de ajo","valor":4000},{"nombre":"Ocaccia","valor":8000},{"nombre":"Pretzels","valor":4500},{"nombre":"Bol de queso","valor":2500},{"nombre":"Empanadas","valor":2000},{"nombre":"Pan de centeno","valor":5500},{"nombre":"Pan de aceitunas","valor":4500},{"nombre":"Pan de hierbas","valor":4000}]), "Promociones":list ([ {"indice":0,"nombre":"Descuento del 9% por comprar 5","unidades":5, "descuento": 0.10} , {"indice":0,"nombre":"Descuento del 10.5% por comprar 15 unidades","unidades":5, "descuento": 0.105} ]) },
#categoria DOS   
    "Pasteles":{"producto": list([{"nombre": "Torta de chocolate", "valor":40000},{"nombre":"Tarta de manzana","valor":35000},{"nombre":"Torta de zanahoria","valor":45000},{"nombre":"Tarta red Velvet","valor":40000},{"nombre":"Tarta de limón","valor":50000},{"nombre":"Torta de queso","valor":45000},{"nombre":"Torta de Frutas","valor":50000},{"nombre":"Tarta Sacher","valor":55000},{"nombre":"Torta 3 leches","valor":40000},{"nombre":"Torta de nueces y caramelo","valor":50000} ]), "Promociones":list ([ {"indice":0,"nombre":"Descuento del 50% por ser tu cumpleaños","unidades":1, "descuento": 0.50} , {"indice":0,"nombre":"Descuento del 20% por comprar 2 unidades","unidades":2, "descuento": 0.05} ]) }
})#cierre deldiccionario

#UNA VEZ ORGANIZADA LA INFO PODEMOS

#Tenemos que meter un algoritmo que muestre primero las categorias: comenzamos con un mensaje de bienvenida

# Mensaje del banner
mensaje_banner = "Hola usuario, bienvenido a Panadería Carlos, ¿qué se te antoja :D?"

# Imprimir el banner)(con solo un print basta pero me gusta decorar y busque este comando en chat gtp)
print("*" * 70)
print("*" + " " * 68 + "*")
print("*" + mensaje_banner.center(68) + "*")
print("*" + " " * 68 + "*")
print("*" * 70)

#queremos mostrar las categorias para esp primero sacaremos las keys(las claves=categorias(dulces,salados,pasteles))
listaCategoria=menu.keys()
#ahora esas claves las volvemos una lista para orden de los datos 
listaCategoria=list(listaCategoria)
#Agregamos el bucle de for i,val para enumerar de modo que queden = 0. dato, 1.dato ...
for i, val in enumerate(listaCategoria):
    #finalmente imprimimos el catálogo: en la expresión
    print(f"{i}. {val}")
#ahora debemos hacer que se pueda escojer una opcion de las 3:
#ahora crearemos una variable para seleccionar la categoria (APARTE, OJO CON LAS SANGRÍAS Y QUE NO SE CONECTE CON LA EXPRESIÓN ANTERIOR)
SelecciónlistaCategoria=int(input())#la expreción int(input()) nos deja seleccionar a partir de un número entero y este se guarda de la variable "SelecciónlistaCategoria"
#una vez terminada la selección tendremos que mostrar la información dentro de esa categoría, usaremos una expresión que me muestre solo los productos de esa categoría seleccionada
#primero definir esta variable de los productos de la categoria
# Mostrar los productos de la categoría seleccionada
productos = menu[listaCategoria[SelecciónlistaCategoria]]["producto"]
#pero queremos que se muestren de manera enumerada sino toda la lista se verá tal cual esté escrita dentro del código, con llaves y todo {}
#tenemos una variable con la lista de las categorias y la selección guardada, linea de código 42, 
#para imprimirla tomaremos un "mensaje"+la lista de la categoria para posicionarnos y la selecci[on de la lista para acceder a esos datos, todo esto dentro de corcheas para tocar enumeraciones y posiciones
print("Productos de la categoría", listaCategoria[SelecciónlistaCategoria])#así quedaría
#ahora toca poner la condición para que pueda ser puesto en lista junto con una secuencia de el número+.+elproducto+elprecio
for i, producto in enumerate(productos):#la condición para enumerar
    #por ultimo imprimir el listado de la categoría
    print(f"{i}. {producto['nombre']}: ${producto['valor']}") #se imprime todo ordenado y más presentable
#ahora tenemos que seleccionar algún producto
ProductoSeleccionado=int(input("Seleccione un producto: "))#de esta manera creamos una variable y selección al mismo tiempo
#ahora toca pedir una cantidad al usuario del producto escojído para calcular un precio diferente
Cantidaddeproducto=int(input("Cuantas unidades deseas: "))
#deberiamos mostrarle al usuario ahora cuanto es el nuevo valor que tendrá su pedido junto mostrar que producto
preciodelproducto=menu[listaCategoria[SelecciónlistaCategoria]]["producto"][ProductoSeleccionado]["valor"]
#Creamos una variable con el precio total que sería la operación de multiplicar la cantidad por el precio
Preciototal=preciodelproducto*Cantidaddeproducto

print(Preciototal)