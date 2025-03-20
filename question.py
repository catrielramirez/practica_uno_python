import random
import sys


# Preguntas para el juego
questions = [
 "¿Qué función se usa para obtener la longitud de una cadena en Python?",
 "¿Cuál de las siguientes opciones es un número entero en Python?",
 "¿Cómo se solicita entrada del usuario en Python?",
 "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
 "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
 ]
 
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
 ("size()", "len()", "length()", "count()"),
 ("3.14", "'42'", "10", "True"),
 ("input()", "scan()", "read()", "ask()"),
 (
 "// Esto es un comentario",
 "/* Esto es un comentario */",
 "-- Esto es un comentario",
 "# Esto es un comentario",
 ),
 ("=", "==", "!=", "==="),
 ]
 
# Índice de la respuesta correcta para cada pregunta, en el mismo orden que las preguntas 
correct_answers_index = [1, 2, 0, 3, 1]

# Se agrupan preguntas, respuestas y respuestas correctas en tuplas y se seleccionan 3, con posible repeticion
questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), 3)
print(len(questions_to_ask))
print(questions_to_ask)
puntaje = 0

 # El usuario deberá contestar 3 preguntas
for question, posible_answers, correct_index in questions_to_ask:
  # Se muestra la pregunta y las respuestas posibles
  print(question)
 
  for i, answer in enumerate(posible_answers, start=1):
    print(f"{i}. {answer}")
 
  # El usuario tiene 2 intentos para responder correctamente
  for intento in range(2):
    try:
      user_answer = int(input("Respuesta: "))-1
      # verifica si esta en rango
      if user_answer < 0 or user_answer >= len(posible_answers):
        print("Respuesta no valida")
        sys.exit(1)
    except ValueError:
      print("Respuesta no valida")
      sys.exit(1)

    # Se verifica si la respuesta es correcta
    if user_answer == correct_index:
      print("¡Correcto!")
      puntaje += 1
      print(f"Tiene {puntaje} puntos")
      break
    else:
      if puntaje != 0:
        puntaje -= 0.5
        print(f"Incorrecto. Se descontaron 0.5 puntos. Tiene {puntaje} puntos")
      else:
        print("Incorrecto")
  else:
    # Si el usuario no responde correctamente después de 2 intentos,
    #      # se muestra la respuesta correcta
    print("Incorrecto. La respuesta correcta es:")
    print(posible_answers[correct_index])
    # Se imprime un blanco al final de la pregunta
    print()
print("Termino la triada de preguntas!")
print(f"Obtuvo {puntaje} puntos")