

#crear nuestra información completa y detallada, en este caso 3 categorías con 3 promociones cada una
#crear código que muestre, deje seleccionar, muestre valor, deje contar cuanto dinero, de vueltos y deje comprar promociones



#Diccionario: bloque que retendrá toda nuestra información
menu= dict({

#categorías(En Python, cuando defines un diccionario, cada par clave-valor debe estar separado por una coma ,)
#dentro de la categoria asignaremos una variable de producto como lista

#ahora agregamos la info dentro de estas para tener pares de Clave-Valor
#Dentro de las claves-valor irá la información del nombre del producto-precio del producto.(números no llevan comillas doblres por ser valores numéricos)
#Categoria CERO
    #ahora agregar como segunda lista acompañando la categoría Dulces son las Promociones, ATENCIÓN la misma categoria tiene 2 listas de la siguiente manera = >>>nombre diccionatoi=dict({ "nombrelista":list{["":""]}, "nombrelista":list{["":""]} })

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

# Imprimir el banner
print("*" * 70)
print("*" + " " * 68 + "*")
print("*" + mensaje_banner.center(68) + "*")
print("*" + " " * 68 + "*")
print("*" * 70)

#queremos mostrar las categorias sacaremos las keys 
listaCategoria=menu.keys()
listaCategoria=list(listaCategoria)
for i, val in enumerate(listaCategoria):
    print(f"{i}. {val}")
