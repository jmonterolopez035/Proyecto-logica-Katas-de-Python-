#1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
def frecuencia_letras(texto):
    # Primero, quitamos los espacios en blanco y lo pasamos todo a minúsculas para no duplicar letras (A != a)
    texto_limpio = texto.replace(" ", "").lower()
    
    # Creamos un diccionario vacío donde guardaremos el resultado
    frecuencias = {}
    
    # Recorremos cada letra del texto limpio
    for letra in texto_limpio:
        if letra in frecuencias:
            frecuencias[letra] += 1 # Si la letra ya está en el diccionario, sumamos 1
        else:
            frecuencias[letra] = 1  # Si es la primera vez que la vemos, la inicializamos a 1
            
    return frecuencias


#2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
def doblar_valores(lista_numeros):
    # map() aplica una función a cada elemento de una lista. 
    # Usamos 'lambda x: x * 2' que es una función anónima (rápida) que simplemente multiplica por 2.
    # Finalmente, convertimos el resultado de map() de vuelta a una lista con list()
    lista_doble = list(map(lambda x: x * 2, lista_numeros))
    return lista_doble


#3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
def buscar_palabras(lista_palabras, objetivo):
   #Usamos lista de comprensión que lo que hace es"Devuélveme la 'palabra' por cada 'palabra' en la lista original, SOLO SI el 'objetivo' está dentro de esa 'palabra'".
    return [palabra for palabra in lista_palabras if objetivo in palabra]


#4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
def diferencia_listas(lista1, lista2):
    # map() también puede recibir múltiples listas. 
    # La función lambda toma 'x' de la lista1 e 'y' de la lista2 en cada iteración y los resta.
    return list(map(lambda x, y: x - y, lista1, lista2))


#5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
#que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.
def evaluar_notas(lista_notas, nota_aprobado=5):
    # Calculamos la media
    media = sum(lista_notas) / len(lista_notas)
    
    # Usamos un condicional para determinar el estado
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
        
    # Retornamos los valores entre paréntesis para que sea una Tupla, tal como pide el ejercicio
    return (media, estado)


#6. Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial(n):
    # Condición base: si el número es 0 o 1, el factorial siempre es 1
    if n == 0 or n == 1:
        return 1
    # Recursividad: multiplicamos el número por el factorial del número anterior
    else:
        return n * factorial(n - 1)


#7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
def tuplas_a_strings(lista_tuplas):
    # map() aplica la función 'str' a cada tupla de la lista
    return list(map(str, lista_tuplas))


#8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
#o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.
def dividir_numeros():
    # El bloque try intenta ejecutar el código. Si falla, salta a los 'except'
    try:
        # Pedimos los números por pantalla (input) y los convertimos a decimales (float)
        num1 = float(input("Introduce el dividendo: "))
        num2 = float(input("Introduce el divisor: "))
        
        resultado = num1 / num2
        print(f"División exitosa. El resultado es: {resultado}")
        
    # Si float() falla porque el usuario metió letras:
    except ValueError:
        print("Error: Por favor, ingresa un valor puramente numérico.")
        
    # Si la división falla porque el divisor es 0:
    except ZeroDivisionError:
        print("Error: Es imposible dividir por cero.")


#9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
#excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()
def mascotas_permitidas(lista_mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    
    # filter() se queda solo con los elementos que cumplen la condición.
    # La condición (lambda) es que la mascota NO esté en la lista de prohibidas.
    return list(filter(lambda mascota: mascota not in prohibidas, lista_mascotas))


#10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
def promedio_lista(lista_numeros):
    # Comprobamos si la lista tiene longitud 0 (está vacía)
    if len(lista_numeros) == 0:
        # raise fuerza a Python a lanzar un error con nuestro mensaje personalizado
       raise ValueError("La lista está vacía.")
    # Si no está vacía, calculamos el promedio: suma total entre la cantidad de elementos
    return sum(lista_numeros) / len(lista_numeros)


#11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
def solicitar_edad():
    try:
        # Pedimos la entrada y tratamos de convertirla a entero (int)
        edad = int(input("Por favor, introduce tu edad: "))
        
        # Comprobamos si la edad está fuera del rango lógico
        if edad < 0 or edad >= 120:
            # Usamos 'raise' para lanzar nuestro propio error si la edad es irreal
            raise ValueError("La edad introducida debe estar entre 0 y 120 años.")
            
        print(f"Edad registrada correctamente: {edad} años.")
        
    except ValueError as error:
        # Esto captura tanto si meten letras (falla el int()) como si saltó nuestro 'raise'
        print(f"Entrada inválida. {error}")


#12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()
def longitud_palabras(frase):
    # El método .split() divide la frase en una lista de palabras (separando por espacios)
    palabras = frase.split()
    
    # Aplicamos la función integrada 'len' (que mide longitudes) a cada palabra de la lista
    return list(map(len, palabras))


#13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()
def mayus_minus(caracteres):
    # Convertimos la lista de caracteres a un 'set'.
    caracteres_unicos = set(caracteres)
    
    # Creamos la lista de tuplas usando map y una función lambda
    return list(map(lambda letra: (letra.upper(), letra.lower()), caracteres_unicos))


#14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()
def empezar_con_letra(lista_palabras, letra_inicial):
    # filter() evalúa cada palabra. .startswith() comprueba si empieza por la letra dada.
    # Pasamos todo a minúsculas (.lower()) para que no importe si buscan 'A' o 'a'
    return list(filter(lambda palabra: palabra.lower().startswith(letra_inicial.lower()), lista_palabras))


#15. Crea una función lambda que sume 3 a cada número de una lista dada.
# Usamos map() para recorrer la lista y una lambda interna para sumar 3 a cada elemento 'x'.
sumar_tres = lambda lista: list(map(lambda x: x + 3, lista))


#16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()
def palabras_mas_largas(texto, n):
    palabras = texto.split() # Separamos el texto en una lista de palabras
    # filter() se queda solo con las palabras cuya longitud (len) sea mayor que n
    return list(filter(lambda palabra: len(palabra) > n, palabras))


#17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce()
def lista_a_numero(digitos):
    # reduce() va acumulando. Si recibe [5, 7, 2]:
    # Paso 1: 5 * 10 + 7 = 57. Paso 2: 57 * 10 + 2 = 572.
    return reduce(lambda a, b: a * 10 + b, digitos)

#18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
#(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()
def filtrar_sobresalientes():
    # Creamos la lista de diccionarios solicitada
    estudiantes = [
        {"nombre": "Alba", "edad": 20, "calificacion": 95},
        {"nombre": "Juan", "edad": 22, "calificacion": 85},
        {"nombre": "Julio", "edad": 21, "calificacion": 92}
    ]
    # Filtramos accediendo a la clave 'calificacion' del diccionario
    return list(filter(lambda estudiante: estudiante["calificacion"] >= 90, estudiantes))


#19. Crea una función lambda que filtre los números impares de una lista dada.
filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))


#20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()
def solo_enteros(lista_mezclada):
    # type(x) == int comprueba que el elemento sea estrictamente un número entero
    return list(filter(lambda x: type(x) == int, lista_mezclada))


#21. Crea una función que calcule el cubo de un número dado mediante una función lambda
# Para elevar a una potencia tenemos que usar el doble asterisco **
cubo = lambda x: x ** 3


#22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .
#importamos libreria
from functools import reduce
def producto_total(lista_numeros):
    # reduce() va multiplicando cada elemento por el acumulado anterior
    return list(filter(lambda x: isinstance(x, int) and not isinstance(x, bool), lista_numeros))


#23. Concatena una lista de palabras.Usa la función reduce() .
def concatenar_palabras(lista_palabras):
    # Para concatenar textos tenemos que sumar los elementos
    return reduce(lambda x, y: x + y, lista_palabras)


#24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .
def diferencia_total(lista_numeros):
    # reduce() va restando cada elemento al acumulado anterior
    return reduce(lambda x, y: x - y, lista_numeros)


#25. Crea una función que cuente el número de caracteres en una cadena de texto dada.
def contar_caracteres(cadena):
    # len() nos devuelve la longitud de la cadena de texto
    return len(cadena)


#26. Crea una función lambda que calcule el resto de la división entre dos números dados.
# Cuando usamos % calcula el resto de una división
resto_division = lambda x, y: x % y


#27. Crea una función que calcule el promedio de una lista de números.
def calcular_promedio(lista):
    if len(lista) == 0:
        return 0 # Para evitar el error de división por cero si la lista está vacía
    return sum(lista) / len(lista)


#28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def primer_duplicado(lista):
    vistos = set() # Usamos un conjunto para guardar los elementos 
    for elemento in lista:
        if elemento in vistos:
            return elemento # Si ya lo habíamos visto, es el primer duplicado
        vistos.add(elemento) # Si no, lo añadimos a 'vistos'
    return None # Si termina el bucle y no hay duplicados, devolvemos None


#29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
#carácter '#', excepto los últimos cuatro.
def enmascarar_variable(variable):
    texto = str(variable) # Lo ponemos como texto
    if len(texto) <= 4:
        return texto # Si tiene 4 caracteres o menos, no enmascaramos
    # Multiplicamos '#' por el número de caracteres a ocultar, y sumamos los últimos 4
    return '#' * (len(texto) - 4) + texto[-4:]


#30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
#pero en diferente orden.
def son_anagramas(palabra1, palabra2):
    # Limpiamos espacios, pasamos a minúsculas y ordenamos alfabéticamente. 
    # Si al ordenar ambas tienen las mismas letras exactamente, son anagramas.
    str1 = sorted(palabra1.replace(" ", "").lower())
    str2 = sorted(palabra2.replace(" ", "").lower())
    return str1 == str2


#31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
#esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.
def buscar_nombre():
    # Pedimos la lista y la separamos por comas
    entrada = input("Ingresa una lista de nombres: ")
    nombres = [n.strip() for n in entrada.split(",")] # Limpiamos los espacios
    
    nombre_buscado = input("Ingresa el nombre a buscar: ").strip()
    
    if nombre_buscado in nombres:
        print("El nombre fue encontrado en la lista.")
    else:
        # Si no está, se fuerza el mensaje de error
        raise ValueError("Excepción: El nombre no se encuentra en la lista.")


#32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
#devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
def buscar_empleado(nombre, lista_empleados):
    # Una lista podria ser así: [{"nombre": "Ana", "puesto": "Gerente"}, ...]
    for empleado in lista_empleados:
        if empleado.get("nombre") == nombre:
            return empleado.get("puesto")
    return "La persona no trabaja aquí."


#33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
# map() tomará un elemento de cada lista y la función lambda los sumará
sumar_listas = lambda l1, l2: list(map(lambda x, y: x + y, l1, l2))


#34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
#crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.
#Código a seguir:
#1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
#2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
#3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
#4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
#5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
#6. Implementar el método
#info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las
#mismas.
#Caso de uso:
#1. Crear un árbol.
#2. Hacer crecer el tronco del árbol una unidad.
#3. Añadir una nueva rama al árbol.
#4. Hacer crecer todas las ramas del árbol una unidad.
#5. Añadir dos nuevas ramas al árbol.
#6. Retirar la rama situada en la posición 2.
#7. Obtener información sobre el árbol.
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = [] # Lista vacía de ramas
        
    def crecer_tronco(self):
        self.tronco += 1
        
    def nueva_rama(self):
        self.ramas.append(1) # Agregamos rama de longitud 1
        
    def crecer_ramas(self):
        # Recorremos la lista de ramas
        for i in range(len(self.ramas)):
            self.ramas[i] += 1
            
    def quitar_rama(self, posicion):
        try:
            self.ramas.pop(posicion)
        except IndexError:
            print("Esa posición de rama no existe.")
            
    def info_arbol(self):
        return f"Tronco: {self.tronco}, Número de ramas: {len(self.ramas)}, Longitudes: {self.ramas}"


#36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
#corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
#Código a seguir:
#1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
#2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no
#poder hacerse.
#3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual.
#Lanzará un error en caso de no poder hacerse.
#4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
#Caso de uso:
#1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
#2. Agregar 20 unidades de saldo de "Bob".
#3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
#4. Retirar 50 unidades de saldo a "Alicia".
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente 
        
    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError(f"Error: {self.nombre} no tiene suficiente saldo.")
        self.saldo -= cantidad
        
    def agregar_dinero(self, cantidad):
        self.saldo += cantidad 
        
    def transferir_dinero(self, otro_usuario, cantidad):
        if otro_usuario.saldo < cantidad:
            raise ValueError(f"Error: {otro_usuario.nombre} no tiene fondos suficientes.")
        otro_usuario.retirar_dinero(cantidad)
        self.agregar_dinero(cantidad)


#37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,
#reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto .
#Código a seguir:
#1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene
#que devolver un diccionario.
#2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene
#que devolver el texto con el remplazo de palabras.
#3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra
#eliminada.
#4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un
#número de argumentos variable según la opción indicada.
#Caso de uso:
#Comprueba el funcionamiento completo de la función procesar_texto
def contar_palabras(texto):
    diccionario = {}
    for palabra in texto.split():
        diccionario[palabra] = diccionario.get(palabra, 0) + 1
    return diccionario

def reemplazar_palabras(texto, original, nueva):
    return texto.replace(original, nueva)

def eliminar_palabra(texto, palabra):
    # Utilizamos el método replace para eliminar la palabra
    return texto.replace(palabra, "").replace("  ", " ").strip()

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1]) 
    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])


#38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
def momento_del_dia():
    hora = int(input("Introduce la hora (formato 0-23): "))
    if 6 <= hora <= 12:
        print("Es de día")
    elif 12 < hora <= 20:
        print("Es de tarde")
    elif (20 < hora <= 23) or (0 <= hora < 6):
        print("Es de noche")


#39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
#Las reglas de calificación son:
#- 0 - 69 insuficiente
#- 70 - 79 bien
#- 80 - 89 muy bien
#- 90 - 100 excelente
def calificacion_texto(nota):
    if 0 <= nota <= 69:
        return "insuficiente"
    elif 70 <= nota <= 79:
        return "bien"
    elif 80 <= nota <= 89:
        return "muy bien"
    elif 90 <= nota <= 100:
        return "excelente"
    else:
        return "Nota incorrecta"



#40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
#"triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).
#importamos libreria
import math
def area_figura(figura, datos):
    figura = figura.lower()
    if figura == "rectangulo":
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        radio = datos[0] # La tupla solo tendrá un dato
        return math.pi * (radio ** 2)
    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2



#41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
#monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo
#siguiente:
#1. Solicita al usuario que ingrese el precio original de un artículo.
#2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
#3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
#4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
#a cero). Por ejemplo, descuento de 15€.
#5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
#6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
#programa de Python.
def tienda_online():
    precio = float(input("Ingresa el precio del artículo: "))
    tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()

    if tiene_cupon in ["sí", "si"]: 
        valor_cupon = float(input("Ingresa el valor del cupón: "))
        if valor_cupon > 0:
            precio_final = precio - valor_cupon
            if precio_final < 0:
                precio_final = 0
            print(f"Descuento aplicado. El precio final es: {precio_final}€")
        else:
            print(f"El cupón no es válido. Precio: {precio}€")
    elif tiene_cupon == "no":
        print(f"El precio final es: {precio}€")
    else:
        print("Respuesta no reconocida.")