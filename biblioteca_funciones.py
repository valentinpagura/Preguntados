import pygame  ##1 = Perdiste; 2 = Ultima vida; 3 = Normal; 4 = Ganaste; 5 = Juego terminado
import json

def btn_preguntas(preguntas, num_pregunta_actual, var_pregunta, var_text_opcion1, var_text_opcion2, var_text_opcion3):
    '''Devuelve el número de la pregunta actual, el elemento actual de la lista junto con todos sus valores, la pregunta actual, la primera, segunda y tercer opción y el estado actual del juego, siendo 3 cada vez que aparece una nueva pregunta. Cuando se terminan las preguntas, el número de la pregunta actual y el elemento actual de la lista no se modifican debido a que no son necesarios usarlos posteriormente, la pregunta actual cambia a un texto final, las tres opciones cambian a tres cadenas vacías y el estado cambia a 5.'''
    contador = 0 #indica posicion
    ind = 0 #cuantas veces recorre por completo la lista preguntas
    for lista in preguntas: #Itera sobre la lista preguntas para contar cuántas preguntas hay en total y para encontrar la pregunta actual según num_pregunta_actual.
        ind += 1
    if ind + 1 == num_pregunta_actual: #Si num_pregunta_actual es igual a ind + 1, significa que num_pregunta_actual está apuntando a una posición fuera del rango de la lista preguntas
        return num_pregunta_actual, lista, "¡LLegaste al final! ¿Cuál es tu nombre?", "", "", "", 5
    for lista in preguntas: #aca va recorriendo la lista de preguntas 
        contador += 1
        if contador == num_pregunta_actual:   #Si la función no está en la última pregunta, avanza al siguiente conjunto de preguntas:
            num_pregunta_actual += 1 #Incrementa num_pregunta_actual para apuntar a la siguiente pregunta.
            var_pregunta = lista['pregunta'] #Actualiza var_pregunta, var_text_opcion1, var_text_opcion2, var_text_opcion3 con los datos de la siguiente pregunta.
            var_text_opcion1 = lista['a']
            var_text_opcion2 = lista['b']   #creo un contador que cuente las veces que se ejecuto el for y si coincide con el número de la pregunta actual (num_pregunta_actual) se elige esa pregunta y la devuelve en el return
            var_text_opcion3 = lista['c']
            return num_pregunta_actual, lista, var_pregunta, var_text_opcion1, var_text_opcion2, var_text_opcion3, 3 #Devuelve estos valores junto con num_pregunta_actual y un estado 3, que puede indicar que el juego está en curso.
        
def respuesta_correcta(pregunta_actual, opcion, estado, score, var_texto_opcion, sonido_correcto, sonido_incorrecto):
    '''Esta función devuelve el color del botón seleccionado, el estado actual del juego (siendo 4 si la opción seleccionada es correcta, 2 si el usuario tiene una última oportunidad, y 1 cuando el usuario ha perdido todas sus oportunidades), el puntaje total acumulado, y una cadena vacía si la opción seleccionada era incorrecta.'''
    match estado: #esta función maneja la evaluación de respuestas en el juego
        case 3: #Comprueba si la opcion seleccionada por el usuario coincide con pregunta_actual['correcta'] (la opción correcta).
            if pregunta_actual['correcta'] == opcion:
                score += 10
                estado = 4
                sonido_correcto.play()
                return (4, 109, 0), estado, score, var_texto_opcion #Retorna una tupla con el color del botón verde (4, 109, 0), el nuevo estado, el score actualizado y var_texto_opcion.
            else: 
                estado -= 1 #si es incorrecta reduce el estado en 1
                var_texto_opcion = ""
                sonido_incorrecto.play()                                   #una tupla es un conjunto ordenado e inmutable de elementos del mismo o diferente tipo
                return (21, 116, 205), estado, score, var_texto_opcion #Retorna una tupla con el color del botón azul (21, 116, 205), el nuevo estado, el score sin cambios y var_texto_opcion.
        case 2:
            if pregunta_actual['correcta'] == opcion: #aca se contempla que es la ultima oportunidad del usuario
                score += 5
                estado = 4
                sonido_correcto.play()
                return (4, 109, 0), estado, score, var_texto_opcion
            else:
                estado -= 1
                var_texto_opcion = ""
                sonido_incorrecto.play()
                return (21, 116, 205), estado, score, var_texto_opcion  
            
def fun_escribir_nombre(event, lista_nombre_caracter, var_textbox_nombre):
    '''Función que se encarga de escribir el nombre del usuario y almacenar cada caracter en una lista. Dicha lista servirá para eliminar el último caracter si es que el usuario desea borrar la última letra que escribió. Devuelve la lista y el texto escrito.'''
    if event.key != 8 and event.key != 9 and event.key != 13: #8 para retroceso, 9 para tabulación, 13 para enter
        if event.unicode != "": #Si event.unicode no está vacío
            if event.key != 32 or (event.key == 32 and var_textbox_nombre != ""): #Si la tecla no es un espacio (32) o si es un espacio pero var_textbox_nombre no está vacío (esto evita que se agreguen espacios al principio):
                if len(lista_nombre_caracter) <= 29:
                    lista_nombre_caracter.append(event.unicode) #Agrega event.unicode a lista_nombre_caracter.
                    var_textbox_nombre += event.unicode #Concatena event.unicode a var_textbox_nombre. #cadena de texto donde se está construyendo el contenido completo del nombre que el usuario está ingresando.
    if event.key == 8:
        if len(lista_nombre_caracter) != 0:
            del lista_nombre_caracter[len(lista_nombre_caracter)-1]
            var_textbox_nombre = ""
            for caracter in lista_nombre_caracter:
                var_textbox_nombre += caracter
    return lista_nombre_caracter, var_textbox_nombre

def exportar_json(var_textbox_nombre, score, lista_puntaje):
    '''Función que se encarga de guardar en un archivo json una lista anidada del nombre del usuario y su respectivo puntaje.
    Devuelve dicha lista anidada para uso posterior.'''
    puntaje = []  # Crear una lista vacía llamada puntaje
    puntaje.append(var_textbox_nombre)  # Agregar el nombre de usuario a la lista puntaje
    puntaje.append(score)  # Agregar el puntaje del usuario a la lista puntaje
    lista_puntaje.append(puntaje)  # Agregar la lista puntaje a la lista principal lista_puntaje


    if lista_puntaje: #Se verifica si lista_puntaje tiene algún contenido (es decir, no está vacía)
        with open('puntaje.json', 'w') as archivo:
            json.dump({"puntaje": lista_puntaje}, archivo, indent=4) #Se utiliza json.dump() para escribir lista_puntaje en formato JSON en el archivo.
                                                            #sangria
    return lista_puntaje

def btn_mejores_puntajes(puntajes):
    '''Devuelve la lista anidada obtenida en la función exportar_json() ordenada de mayor a menor según las puntuaciones.'''
    lista_temporal = []
    for nombre, puntaje in puntajes: #En esta parte, se recorre cada tupla (nombre, puntaje) en la lista puntajes. Cada tupla se convierte en una lista [puntaje, nombre] y se añade a lista_temporal.
        lista_temporal.append([puntaje, nombre])
    lista_temporal.sort(reverse=True) #Aquí, lista_temporal se ordena en orden descendente 
    lista_ordenada = []
    for puntaje, nombre in lista_temporal: #Después de ordenar lista_temporal, se recorre nuevamente para revertir el orden de los elementos de cada lista [puntaje, nombre] a [nombre, puntaje]
        lista_ordenada.append([nombre, puntaje])
    return lista_ordenada #la función devuelve lista_ordenada, que es una lista de listas donde cada sublista contiene un nombre y su puntaje correspondiente

def btn_silenciar_sonido(musica_fondo, imagen_sonido, sonido):
    '''Función que se encarga de silenciar el sonido de fondo. Devuelve el volumen actualizado, la nueva imagen del botón y el estado del sonido, siendo True si el volumen es 100 y False si el volumen es 0.'''
    if sonido:
        musica_fondo = pygame.mixer.music.set_volume(0)
        imagen_sonido = pygame.image.load("13e1104c037f73a11616f5859cb7d5b4-boton-de-volumen-icono-de-circulo-volumen-bajo.webp")
        sonido = False
    else:
        musica_fondo = pygame.mixer.music.set_volume(100)
        imagen_sonido = pygame.image.load("13e1104c037f73a11616f5859cb7d5b4-boton-de-volumen-icono-de-circulo-volumen-bajo.webp")
        sonido = True
    return musica_fondo, imagen_sonido, sonido