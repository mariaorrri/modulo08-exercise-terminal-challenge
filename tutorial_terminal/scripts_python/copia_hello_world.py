from datetime import datetime
fecha_hora_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

with open('/workspaces/modulo08-exercise-terminal-challenge/tutorial_terminal/res/text.txt' , 'a') as archivo:
	archivo.write(f'Tarea finalizada a las {fecha_hora_actual}')

