import random

# set de palabras temporal
palabras = ("horca", "paseo", "estudio", "poema", "pito",
            "verso", "vispera", "oreja", "medico", "velo",
            "mareo", "pelicula", "oferta", "pesado", "casa",
            "hogar", "escalon", "fornido", "higo", "sopa", "amor", "poder",
            "inflable", "mestizo", "espejo", "madera",
            "erizo", "reloj", "computacion", "python", "visa",
            "valor", "solar", "sentido", "zumo", "cena", "plato",
            "pais", "seda", "mariposa", "salida", "nuevo", "escalon",
            "hule", "hierro", "helado", "falso", "fuego",
            "cepillo", "frijol", "fiesta", "iman", "litro", "lago",
            "lunes", "domingo", "mentira", "negro", "nuevo", "nido",
            "manos", "oreja", "ruido")


# Se crea la lista de las letras posteadas
palabra_adivina = random.choice(palabras)
guiones = ("-" * len(palabra_adivina))
palabra_oculta = list(guiones)

inputs_palabras = []
inputs_palabras_string = ""

contador = 1

# se establece la cantidad de oportunidades, len()-2.
oportunidades = len(palabra_adivina) - 2

y = len(palabra_adivina)-2




# INICIO DEL JUEGO
empezar = input("Quieres jugar ADIVINA LA PALABRA?   SI/NO = ")

empezar_upp = empezar.upper()

jugar_again_upp = "SI"


# juego
while empezar_upp == "SI" and jugar_again_upp == "SI":

  palabra_adivina = random.choice(palabras)
  guiones = ("-" * len(palabra_adivina))
  palabra_oculta = list(guiones)

  # se establece la cantidad de oportunidades, len()-2.
  oportunidades = len(palabra_adivina) - 2
  y = len(palabra_adivina)-2
  
  contador = 1

  while contador <= y:
      
      letra_posteada = input(
          "ingrese una letra para completar la palabra secreta =  ")
      
     
      # se adiciona a la lista de letras posteadas por el jugador

      inputs_palabras.append(letra_posteada.upper())
      

      
      if output := letra_posteada.upper() in palabra_adivina.upper():
          for pos, char in enumerate(palabra_adivina):
             if char == letra_posteada:
                 palabra_oculta[pos] = char
                 palabra_adivinada = list(palabra_oculta)
                 palabra2 = "".join(palabra_adivinada)
                 print(palabra2)
      
      if not letra_posteada in palabra_adivina:
        print("LETRA INCORRECTA, INTENTA OTRA LETRA...")
      
      
      # se descuentan las oportunidades restantes
      print(f"Te quedan {y-contador} oportunidades")

      contador = contador + 1
   

  else:

      palabra_oculta.clear()
      
      pregunta_final = input("Si Adivinaste la palabra, escribela = ? ")

      if pregunta_final.lower() == palabra_adivina.lower():

        uni = "\U0001F3C6"

        print(f"{uni} ERES UN GENIO!!, LA PALABRA SECRETA ES {pregunta_final}")

      else:

        print("\U0001F625", "MEJOR SUERTE PARA LA PROXIMA")
      
  jugar_again = input("quieres jugar de nuevo? SI/NO = ")

  jugar_again_upp = jugar_again.upper()





  
  
 

