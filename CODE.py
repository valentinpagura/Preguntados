import pygame
from datos import lista
from biblioteca_funciones import *


preguntas = lista

pygame.init() #Se inicializa pygame

pygame.display.set_caption("Preguntados")

#Imagenes
imagen_fondo = pygame.image.load("leia.jpg")
imagen_fondo = pygame.transform.scale(imagen_fondo, (1280, 720))
imagen_juegof = pygame.image.load("star-wars-background-darth-vader-darth-vader-wallpaper-preview.webp")
imagen_juegof = pygame.transform.scale(imagen_juegof, (1280, 720))
imagen_sonido = pygame.image.load("13e1104c037f73a11616f5859cb7d5b4-boton-de-volumen-icono-de-circulo-volumen-bajo.webp")
imagen_sonido = pygame.transform.scale(imagen_sonido, (30, 30))
imagen_personaje = pygame.image.load("deoqh2x-3e8ee082-5dd9-4531-b879-f5f0fb5800df.webp")
imagen_personaje = pygame.transform.scale(imagen_personaje, (207, 599))


musica_fondo = pygame.mixer.music.load('MUSICA/Star Wars - La musica del Bar.mp3')
sonido_correcto = pygame.mixer.Sound('MUSICA\correct-ding.mp3')
sonido_incorrecto = pygame.mixer.Sound('MUSICA/megaman-x-error.mp3')
musica_fondo = pygame.mixer.music.play(-1)
sonido = True

screen = pygame.display.set_mode([1280, 720])
rect_panel_pregunta = pygame.Rect(24, 195, 1050, 100)
rect_panel_puesto1 = pygame.Rect(381, 189, 800, 43)
rect_panel_puesto2 = pygame.Rect(381, 289, 800, 43)
rect_panel_puesto3 = pygame.Rect(381, 389, 800, 43)
rect_textbox_nombre = pygame.Rect(50, 500, 1050, 5)
rect_boton_jugar = pygame.Rect(90, 220, 290, 70)
rect_boton_puntaje = pygame.Rect(90, 330, 290, 70)
rect_boton_salir = pygame.Rect(90, 440, 290, 70)
rect_boton_volver = pygame.Rect(640, 570, 290, 70)
rect_boton_sonido = pygame.Rect(1235, 678, 30, 25)
rect_boton_opcion1 = pygame.Rect(50, 400, 330, 70)
rect_boton_opcion2 = pygame.Rect(450, 400, 330, 70)
rect_boton_opcion3 = pygame.Rect(850, 400, 330, 70)
rect_boton_reiniciar = pygame.Rect(270, 570, 290, 70)
rect_boton_pregunta = pygame.Rect(670, 570, 290, 70)

font = pygame.font.SysFont("Consolas", 30)
text_btn_start = font.render("Inicio", True, (0, 0, 0))
text_btn_puntaje = font.render("Puntaje", True, (0, 0, 0))
text_btn_salir = font.render("Salir", True, (0, 0, 0))
text_btn_reiniciar = font.render("Reiniciar", True, (0, 0, 0))
text_btn_pregunta = font.render("Pregunta", True, (0, 0, 0))
text_btn_volver = font.render("Volver", True, (0, 0, 0))
text_pregunta = font.render("", True, (0, 0, 0))
text_btn_opcion1 = font.render("", True, (255, 255, 255))
text_btn_opcion2 = font.render("", True, (255, 255, 255))
text_btn_opcion3 = font.render("", True, (255, 255, 255))
textbox_nombre = font.render("", True, (255, 255, 255))
font_score = pygame.font.SysFont("rockwell", 50)
text_score = font_score.render("SCORE", True, (255, 255, 255))
text_score_num = font_score.render("000", True, (255, 255, 255))

font_puntajes_title = pygame.font.SysFont("playbill", 80)
text_puntajes_title = font_puntajes_title.render("PUNTAJES", True, (255, 255, 255))

font_puntaje_puestos = pygame.font.SysFont("rockwell", 25)
text_puesto1 = font_puntaje_puestos.render("1", True, (0, 0, 0))
text_puesto2 = font_puntaje_puestos.render("2", True, (0, 0, 0))
text_puesto3 = font_puntaje_puestos.render("3", True, (255, 255, 255))

font_puntaje_nombres = pygame.font.SysFont("rockwell", 35)
text_nombre1 = font_puntaje_nombres.render("", True, (0, 0, 0))
text_nombre2 = font_puntaje_nombres.render("", True, (0, 0, 0))
text_nombre3 = font_puntaje_nombres.render("", True, (255, 255, 255))
text_puntaje1 = font_puntaje_nombres.render("", True, (0, 0, 0))
text_puntaje2 = font_puntaje_nombres.render("", True, (0, 0, 0))
text_puntaje3 = font_puntaje_nombres.render("", True, (255, 255, 255))

pantalla_actual = "pantalla_principal"
num_pregunta_actual = 1
pregunta_actual = ""
estado = 0 #1 = Perdiste; 2 = Ultima vida; 3 = Normal; 4 = Ganaste; 5 = Juego terminado
score = 0

var_textbox_nombre = ""
lista_nombre_caracter = []

puntajes = []

var_pregunta = ""
var_text_opcion1 = ""
var_text_opcion2 = ""
var_text_opcion3 = ""
var_text_btn_reiniciar = ""
var_text_btn_pregunta = "Pregunta"
var_text_puntaje_nombre1 = ""
var_text_puntaje_nombre2 = ""
var_text_puntaje_nombre3 = ""
var_text_puntaje_num1 = 0
var_text_puntaje_num2 = 0
var_text_puntaje_num3 = 0

color_opcion1 = (21, 116, 205)
color_opcion2 = (21, 116, 205)
color_opcion3 = (21, 116, 205)
color_textbox_nombre = (21, 116, 205)
color_btn_reiniciar = (21, 116, 205)
color_btn_pregunta = (214, 214, 214)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if estado == 5: #juego terminado maneja escrituras de nombres
                lista_nombre_caracter, var_textbox_nombre = fun_escribir_nombre(event, lista_nombre_caracter, var_textbox_nombre)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pantalla_actual == "juego":
                if rect_boton_pregunta.collidepoint(event.pos):
                    if var_text_btn_pregunta == "Pregunta":
                        num_pregunta_actual, pregunta_actual, var_pregunta, var_text_opcion1, var_text_opcion2, var_text_opcion3, estado = btn_preguntas(preguntas, num_pregunta_actual, var_pregunta, var_text_opcion1, var_text_opcion2, var_text_opcion3)
                        if estado == 5:
                            color_opcion1 = (21, 116, 205)
                            color_opcion2 = (21, 116, 205)
                            color_opcion3 = (21, 116, 205)
                            color_textbox_nombre = (255, 255, 255)
                            color_btn_reiniciar = (21, 116, 205)
                            var_text_btn_reiniciar = ""
                            var_text_btn_pregunta = "Aceptar"
                        else:
                            color_opcion1 = (0, 99, 108)
                            color_opcion2 = (0, 99, 108)
                            color_opcion3 = (0, 99, 108)
                            color_textbox_nombre = (21, 116, 205)
                            color_btn_pregunta = (21, 116, 205)
                            var_text_btn_pregunta = ""
                            color_btn_reiniciar = (214, 214, 214)
                            var_text_btn_reiniciar = "Reiniciar"
                    elif var_text_btn_pregunta == "Aceptar":
                        if var_textbox_nombre != "":
                            puntajes = exportar_json(var_textbox_nombre, score, puntajes)
                            pantalla_actual = "pantalla_principal"
                            pregunta_actual = ""
                            num_pregunta_actual = 1
                            estado = 3
                            score = 0
                            var_pregunta = ""
                            var_text_opcion1 = ""
                            var_text_opcion2 = ""
                            var_text_opcion3 = ""
                            var_text_btn_pregunta = "Pregunta"
                            var_text_btn_reiniciar = ""
                            var_textbox_nombre = ""
                            lista_nombre_caracter = []
                            color_opcion1 = (21, 116, 205)
                            color_opcion2 = (21, 116, 205)
                            color_opcion3 = (21, 116, 205)
                            color_btn_pregunta = (214, 214, 214)
                            color_btn_reiniciar = (21, 116, 205)
                            color_textbox_nombre = (21, 116, 205)
                        else:
                            var_pregunta = "El nombre no puede quedar vacío. ¿Cuál es tu nombre?"

                if pregunta_actual != "":
                    if estado == 2 or estado == 3: #ultima vida o estado normal de juego
                        if rect_boton_opcion1.collidepoint(event.pos):
                            color_opcion1, estado, score, var_text_opcion1 = respuesta_correcta(pregunta_actual, 'a', estado, score, var_text_opcion1, sonido_correcto, sonido_incorrecto)
                        if rect_boton_opcion2.collidepoint(event.pos):
                            color_opcion2, estado, score, var_text_opcion2 = respuesta_correcta(pregunta_actual, 'b', estado, score, var_text_opcion2, sonido_correcto, sonido_incorrecto)
                        if rect_boton_opcion3.collidepoint(event.pos):
                            color_opcion3, estado, score, var_text_opcion3 = respuesta_correcta(pregunta_actual, 'c', estado, score, var_text_opcion3, sonido_correcto, sonido_incorrecto)
                    if estado == 1: 
                        match pregunta_actual['correcta']:
                            case 'a':
                                color_opcion1 = (109, 0, 0)
                            case 'b':
                                color_opcion2 = (109, 0, 0)
                            case 'c':
                                color_opcion3 = (109, 0, 0)
                        color_btn_pregunta = (214, 214, 214)
                        var_text_btn_pregunta = "Pregunta"
                    if estado == 4:
                        if pregunta_actual['correcta'] != 'a': #Si la respuesta correcta no es igual a 'a', entonces se cambia el color de la opción 1 y se vacia
                            color_opcion1 = (21, 116, 205)
                            var_text_opcion1 = ""
                        if pregunta_actual['correcta'] != 'b': #""
                            color_opcion2 = (21, 116, 205)
                            var_text_opcion2 = ""
                        if pregunta_actual['correcta'] != 'c': #""
                            color_opcion3 = (21, 116, 205)
                            var_text_opcion3 = ""
                        color_btn_pregunta = (214, 214, 214)
                        var_text_btn_pregunta = "Pregunta"

                if rect_boton_reiniciar.collidepoint(event.pos):
                    if var_text_btn_reiniciar == "Reiniciar":
                        pregunta_actual = ""
                        num_pregunta_actual = 1
                        estado = 3
                        score = 0
                        var_pregunta = ""
                        var_text_opcion1 = ""
                        var_text_opcion2 = ""
                        var_text_opcion3 = ""
                        var_text_btn_pregunta = "Pregunta"
                        var_text_btn_reiniciar = ""
                        color_opcion1 = (21, 116, 205)
                        color_opcion2 = (21, 116, 205)
                        color_opcion3 = (21, 116, 205)
                        color_btn_pregunta = (214, 214, 214)
                        color_btn_reiniciar = (21, 116, 205)
            elif pantalla_actual == "pantalla_principal":
                if rect_boton_jugar.collidepoint(event.pos):
                    pantalla_actual = "juego"
                
                if rect_boton_puntaje.collidepoint(event.pos):
                    contador = 0 #Se usará para rastrear el número de puntajes y controlar cómo se actualizan las variables
                    var_text_puntaje_nombre1 = "---"
                    var_text_puntaje_num1 = ""
                    var_text_puntaje_nombre2 = "---"
                    var_text_puntaje_num2 = ""
                    var_text_puntaje_nombre3 = "---"
                    var_text_puntaje_num3 = ""
                    pantalla_actual = "puntajes"
                    puntajes = btn_mejores_puntajes(puntajes)
                    for puntaje in puntajes:
                        contador += 1 #se incrementa en cada iteración para rastrear la posición del puntaje en la lista 
                        match contador: #0 nombre 1 puntaje
                            case 1:
                                var_text_puntaje_nombre1 = puntaje[0] #se usan indicadores de lo que quiero tomar de la tupla 
                                var_text_puntaje_num1 = puntaje[1]
                            case 2:
                                var_text_puntaje_nombre2 = puntaje[0]
                                var_text_puntaje_num2 = puntaje[1]
                            case 3:
                                var_text_puntaje_nombre3 = puntaje[0]
                                var_text_puntaje_num3 = puntaje[1]
                
                if rect_boton_sonido.collidepoint(event.pos):
                    musica_fondo, imagen_sonido, sonido = btn_silenciar_sonido(musica_fondo, imagen_sonido, sonido)
                
                if rect_boton_salir.collidepoint(event.pos):
                    running = False
            else:
                if rect_boton_volver.collidepoint(event.pos):
                    pantalla_actual = "pantalla_principal"
    
    if pantalla_actual == "pantalla_principal":
        screen.fill((147, 154, 168))
        screen.blit(imagen_fondo, (0, 0))
        pygame.draw.rect(screen, (214, 214, 214), rect_boton_jugar, border_radius=5)
        pygame.draw.rect(screen, (214, 214, 214), rect_boton_puntaje, border_radius=5)
        pygame.draw.rect(screen, (214, 214, 214), rect_boton_salir, border_radius=5)
        pygame.draw.rect(screen, (237, 81, 170), rect_boton_sonido)
        screen.blit(imagen_sonido, (1236, 675))
        screen.blit(text_btn_start, (188, 240))
        screen.blit(text_btn_puntaje, (175, 350))
        screen.blit(text_btn_salir, (199, 460))
    elif pantalla_actual == "juego":
        screen.fill((21, 116, 205))
        screen.blit(imagen_juegof, (0, 0))
        pygame.draw.rect(screen, (255, 255, 255), rect_panel_pregunta, border_radius=15)
        pygame.draw.rect(screen, color_opcion1, rect_boton_opcion1, border_radius=10)
        pygame.draw.rect(screen, color_opcion2, rect_boton_opcion2, border_radius=10)
        pygame.draw.rect(screen, color_opcion3, rect_boton_opcion3, border_radius=10)
        pygame.draw.rect(screen, color_btn_reiniciar, rect_boton_reiniciar, border_radius=5)
        pygame.draw.rect(screen, color_btn_pregunta, rect_boton_pregunta, border_radius=5)
        
        screen.blit(text_score, (50, 80))
        screen.blit(text_score_num, (240, 80))
        screen.blit(text_pregunta, (50, 226))
        screen.blit(text_btn_opcion1, (70, 420))
        screen.blit(text_btn_opcion2, (470, 420))
        screen.blit(text_btn_opcion3, (870, 420))
        screen.blit(text_btn_reiniciar, (333, 590))
        screen.blit(text_btn_pregunta, (746, 590))
        screen.blit(textbox_nombre, (50, 468))
        text_pregunta = font.render(var_pregunta, True, (0, 0, 0))
        text_btn_opcion1 = font.render(var_text_opcion1, True, (255, 255, 255))
        text_btn_opcion2 = font.render(var_text_opcion2, True, (255, 255, 255))
        text_btn_opcion3 = font.render(var_text_opcion3, True, (255, 255, 255))
        textbox_nombre = font.render(var_textbox_nombre, True, (255, 255, 255))
        text_btn_reiniciar = font.render(var_text_btn_reiniciar, True, (0, 0, 0))
        text_btn_pregunta = font.render(var_text_btn_pregunta, True, (0, 0, 0))
        text_score_num = font_score.render(str(score), True, (255, 255, 255))
        pygame.draw.rect(screen, color_textbox_nombre, rect_textbox_nombre, border_radius=0)
    else:
        screen.fill((21, 116, 205))
        pygame.draw.rect(screen, (214, 214, 214), rect_boton_volver, border_radius=5)
        pygame.draw.rect(screen, (207, 155, 0), rect_panel_puesto1, border_radius=3)
        pygame.draw.rect(screen, (240, 255, 247), rect_panel_puesto2, border_radius=3)
        pygame.draw.rect(screen, (83, 47, 0), rect_panel_puesto3, border_radius=3)
        screen.blit(imagen_personaje, (52, 58))
        screen.blit(text_puntajes_title, (678, 58))
        screen.blit(text_btn_volver, (736, 590))
        screen.blit(text_puesto1, (388, 195))
        screen.blit(text_puesto2, (388, 295))
        screen.blit(text_puesto3, (388, 395))
        screen.blit(text_nombre1, (450, 188))
        screen.blit(text_nombre2, (450, 288))
        screen.blit(text_nombre3, (450, 388))
        screen.blit(text_puntaje1, (1110, 188))
        screen.blit(text_puntaje2, (1110, 288))
        screen.blit(text_puntaje3, (1110, 388))
        text_nombre1 = font_puntaje_nombres.render(var_text_puntaje_nombre1, True, (0, 0, 0))
        text_nombre2 = font_puntaje_nombres.render(var_text_puntaje_nombre2, True, (0, 0, 0))
        text_nombre3 = font_puntaje_nombres.render(var_text_puntaje_nombre3, True, (255, 255, 255))
        text_puntaje1 = font_puntaje_nombres.render(str(var_text_puntaje_num1), True, (0, 0, 0))
        text_puntaje2 = font_puntaje_nombres.render(str(var_text_puntaje_num2), True, (0, 0, 0))
        text_puntaje3 = font_puntaje_nombres.render(str(var_text_puntaje_num3), True, (255, 255, 255))
        
    pygame.display.flip()

pygame.quit()