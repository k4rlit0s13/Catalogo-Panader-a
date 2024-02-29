

#crear nuestra información completa y detallada, en este caso 3 categorías con 3 promociones cada una
#crear código que muestre, deje seleccionar, muestre valor, deje contar cuanto dinero, de vueltos y deje comprar promociones



#Diccionario: bloque que retendrá toda nuestra información
menu=dict({

#categorías(En Python, cuando defines un diccionario, cada par clave-valor debe estar separado por una coma ,)
#dentro de la categoria asignaremos una variable de producto como lista

#ahora agregamos la info dentro de estas para tener pares de Clave-Valor
#Dentro de las claves-valor irá la información del nombre del producto-precio del producto.(números no llevan comillas doblres por ser valores numéricos)
#CERO
    "Dulces": {"producto": list([{"nombre":"Croissants", "valor":3500},{"nombre": "Donas", "valor":2000},{"nombre": "Pastelitos", "valor":1500},{"nombre":"Galletas", "valor":7000},{"nombre":"Pan dulce","valor":5000},{"nombre":"Ensaimadas", "valor":6000},{"nombre":"Tartaletas", "valor":4500},{"nombre":"Bizcochos", "valor":2500},{"nombre":"Palmeras", "valor":2000},{"nombre":"Conchas", "valor":2000}])},
#UNO
    "Salados":{"nombre": "", "valor":""},
#DOS
    "Pasteles":{"nombre": "", "valor":""}, 
    
})