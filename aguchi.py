letra=input("ingresá uma letra: ").lower()


frases={
    'a': "a veces me pregunto q hubiera pasado si no te hubiera conocido",
    'b': "bailaria con vos toda la noche  ",
    'c': "como me gusta tu sonrisa",
    'd': "deja de joder con el futbol",
    'e': "espero que estes bien",
    'f': "feliz de tenerte en mi vida",
    'g': "gracias por todo lo que haces por mi",
    'h': "hola, como estas?",
    'i': "imagino un futuro juntos",
    'j': "jamas pense que podria sentir esto por alguien",
    'k': "kiero estar siempre a tu ladoo jjiji",
    'l': "la vida es mejor con vos, aunque te odie a veces",    
    'm': "me haces muy feliz",
    'n': "nunca dejes de sonreir",
    'o': "ojala pudiera verte ahora mismo",
    'p': "pensando en vos todo el dia",
    'q': "quiero que sepas que te amo",
    'r': "recordando nuestro primer beso",
    's': "sos lo mejor que me paso",
    't': "te extraño mucho cuando no estas",
    'u': "un dia sin vos es un dia perdido",
    'v': "vos sos mi persona favorita",
    'w': "why not be happy together?",
    'x': "xq no estas aca conmigo?",
    'y': "y pensar que casi no te hablo ese dia",
    'z': "zarpado lo nuestro, no?"  
}

if letra in frases:
    print(frases[letra])
else:
    print("Letra no válida. Por favor, ingresa una letra de la 'a' a la 'z'.")
#este es un programa que te dice frases romanticas segun la letra que ingreses  
