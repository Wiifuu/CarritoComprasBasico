# Carrito de compras básico

Se necesita crear un carrito de compras basico para ello debo considerar:
- 1.- El usuario puede agregar varios productos indicando el nombre y precio.
- 2.- El sistema calcula el total de la compra.
- 3.- Si el total supera ciertos montos, se aplican descuentos:
  - a) ≥ $100.000 → 20% de descuento.
  - b) ≥ $50.000 → 10% de descuento
  - c) < $50.000 → sin descuento
    
- 4.- El usuario puede ver un resumen con:
    - Lista de productos
    - Total sin descuento
    - Descuento aplicado
    - Total final
      
- 5.- El programa se repite hasta que el usuario decida salir

- 6.- Además de que debo usar:
    - Operadores aritméticos: suma, multiplicación, división.
    - Operadores de comparación: >=, <.
    - Condicionales: if, elif, else.
    - Bucles: while, for.
    - Funciones: con parámetros, retorno, uso de listas.
    - Manejo de errores con try/except.
    - Listas y tuplas para almacenar productos.


# Proceso Lógico y Explicación del código:
- 1.-  Crearé un menu interactivo con 3 opciones para que el usuario ingrese datos:
  - a) Agregar productos
  - b) Ver detalle
  - c) Salir del menu

- 2.-  Para agregar productos crearé una la función "agregar_producto" y como parametro le entregaré una lista vacia.
    En ella pediré en un buce "while True" los datos y los almacenaré", como EXTRA validaré las entradas para que acepte
    solo los datos solicitados, sin cadenas vacias y que los datos numericos sean mayor a 0.

    - Dentro del agregar, retornaré dentro de una tupla el nombre de cada producto y su precio respectivo a la lista que pasamos como parametro.
    Para finalizar por cada ingreso de datos exitoso, preguntaré al usuario si desea continuar ingresando datos o no.

    - En la funcion que comprobará la entrada de datos, le entragaré el dato a comprobar y una variable que servirá para identificar con que opcion estoy trabajando,
    haré uso del try-except para el manejo de error, y además haré uso del "raise ValueError" para en caso fallar por cualquier motivo las condicionales del try FORZAR el error,
    Esto tambien retornara cada dato con su respectivo valor.

- 3.- Luego debo hacer algunos calculos, para ello crearé la funcion "calcular_precio" dandole de parametros la lista con los productos, y retornaré la sumatoria de solo los precios.

    - Tambien debo calcular el descuento y aplicarlo, para ello la funcion "aplicar_descuento" que tendra como parametros el valor retornado por "calcular_precio", por medio de
    condicionales (if, elif, else) veré en que caso me encuetro para retornar el descuento a aplicar

    - Posterior a ello, usaré la funcion "total_compra" con su respectivo parametro la lista de todos los productos, y llamaré a "calcular_precio" y 
    asignaré una variable para almacenar el valor, despues a "aplicar_descuento" para que aplique el descuento, y para finalizar el total_final, que es total-descuento,
    retornando asi esos 3 valores como tupla, pero sin antes transformar dentro de la funcion cada valor a tipo float() para que en el detalle tenga cierto formato al mostrarse.

- 4.- Creamos la funcion "detalle_compra" con parametros la lista de productos, primero comprobamos si la lista se encuentra vacia o no, para mostrar un respectivo mensae o detallar,
    los productos, su precio, total sin descuento, a cuanto corresponde el descuento (mostraremos un cadena en caso que no se aplique el descuento, 
    para ello usaremos condicionales) y el total final.

    - Por ende realizaremos lo siguinte:
        - a)  Por medio de un ciclo (for - in) accederemos a los valores de cada dato, asignando una variable representativa para el nombre del producto y su precio,
            mostramos por pantalla el detalle (al precio lo formatie para que se viera de la siguiente forma $123,123,123.12) y usamos end="" con el valor de '\n' 
            dentro de las comillas dobles para que generara un salto de linea entre cada iteración.
        - b)  Seguimos llamando a la funcion "total_compra" y asignamos variables para cada valor retornado dentro de la tupla (desempaquetamos) para mayor legibilidad dentro del codigo
            Las lineas que siguen se ven confusas pero tiene la siguiente intencion: primero condicionamos si aplica o no el descuento.
            
            - SI NO APLICA, mostramos un mensaje "No aplica Descuento" en vez de decir "Descuento: $0".
            - SI APLICA, mostramos valor del descuento con la variable "descuento" desempaquetada.
            - EXTRA:  si queremos agregar espacios hasta un cierto limite para que todo este en la misma altura usé ":>(numero)" la siguiente sintaxis despues de la variable sirve para eso,
                    se ve confuso y complejo, pero es más sencillo de lo que aparenta.
        - c)  Para finalizar muestra los prints restantes del total sin descuento, el descuento y el total con descuento aplicado.

- 6.-  Volviendo a la función Menu, tengo un bucle (while True), condicionales, if-elif, llamo a las funciones segun corresponda su caso, y además llamo a una funcion que se llama
    "salir_menu" sin parametros, esta simplemente retorna True o False, primero, llama a la funcion "comprobar" y le da como parametros una variable, 
    pero como puede ver, no está almacenada, si no pide el ingreso de la variable al llamar la funcion, y luego el numero que identifica que caso debe usar,
    luego el valor retornado de la funcion "comprobar" lo compara si es igual a "si" explicito, si es el caso retorna True, si no es el caso "retorna" False,

    - ACLARACIÓN: Dentro de la funcion comprobar tengo esto:
        - elif flag in (3, 5) and dato.lower() in ("si", "no"): return dato.lower()
        esto significa, que primero comprueba que caso es, luego que el valor entregado sea alguno de la tupla, y esos valores son "si" y "no", 
        la variable se compara de la siguiente forma: "Si el dato entregado en minusculas se encuentra dentro de la tupla, retornaremos el dato entregado en minisculas"
        entonces si o si, aceptará SOLO como valores unicos "si" y "no", en caso que se ingrese cualquier otro, lo considerará como ValueError, irá al caso correspondiente 
        y pedirá que se ingrese nuevamente el valor.

    - Bueno dentro de las condiciones para la opcion 1 y 2, para poder volver al menu luego de haber llamado a "agregar_producto" o "detalle_compra", 
    si al llamar "menu_salir" su valor retornado es "True", saldra de la funcion llamada con "continue" sin salir de la iteración principal (la del menu) 
    pero parando la ejecucion de los ciclos centro de las funciones llamadas en la linea anterior.

    - y Bueno para la opcion 3, como es para salir, si deseamos imprimimos un mensaje y salimos con "break" o return (al ser una funcion se puede realizar)   
